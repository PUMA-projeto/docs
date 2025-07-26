import yaml
import os
import re
from collections import defaultdict
import inflection

# --- Configurações ---
SWAGGER_FILE_PATH = './swagger.yaml'  # Caminho para o seu arquivo swagger.yaml
MKDOCS_DOCS_DIR = './docs'            # Diretório raiz da sua documentação MkDocs
API_DOCS_SUBDIR = 'produto'               # Subdiretório para os arquivos da API dentro de MKDOCS_DOCS_DIR
MKDOCS_CONFIG_FILE = 'mkdocs.yml'     # Nome do arquivo de configuração do MkDocs

# --- Funções Auxiliares ---

def sanitize_filename(name):
    """Converte uma string em um nome de arquivo seguro."""
    name = inflection.underscore(name)
    name = re.sub(r'[^\w\s-]', '', name).strip().lower()
    name = re.sub(r'[-\s]+', '-', name)
    return name

def format_schema_properties(properties, indent_level=0):
    """Formata as propriedades de um esquema para Markdown."""
    if not properties:
        return ""
    indent = "    " * indent_level
    markdown = f"{indent}| Propriedade | Tipo | Descrição | Exemplo | Obrigatório |\n"
    markdown += f"{indent}|---|---|---|---|---|\n"
    for prop_name, prop_details in properties.items():
        prop_type = prop_details.get('type', 'N/A')
        prop_description = prop_details.get('description', 'N/A').replace('\n', ' ')
        prop_example = prop_details.get('example', 'N/A')
        required = "Sim" if prop_name in properties.get('required', []) else "Não"
        
        # Lidar com tipos 'array' e seus 'items'
        if prop_type == 'array' and 'items' in prop_details:
            items_info = prop_details['items']
            item_type = items_info.get('type', 'object')
            if item_type == 'object' and 'properties' in items_info:
                prop_type += f" (array de {item_type})"
                # Adiciona as propriedades do item em um bloco de código, ou considera um subtítulo
                nested_props_md = format_schema_properties(items_info['properties'], indent_level + 1)
                prop_description += f"\n{indent}**Itens do Array:**\n{nested_props_md}"
            else:
                prop_type += f" (array de {item_type})"

        markdown += f"{indent}| `{prop_name}` | `{prop_type}` | {prop_description} | `{prop_example}` | {required} |\n"
    return markdown

def generate_markdown_content(api_name, endpoints):
    """Gera o conteúdo Markdown para uma página de API."""
    markdown_content = f"# {api_name.replace('-', ' ').title()} API\n\n"
    markdown_content += "Esta página documenta os endpoints relacionados ao serviço de "
    markdown_content += f"**{api_name.replace('-', ' ').title()}**.\n\n"

    for path, methods in endpoints.items():
        for method, details in methods.items():
            summary = details.get('summary', f'{method.upper()} {path}')
            description = details.get('description', 'Nenhuma descrição disponível.').replace('\n', ' ')
            tags = ", ".join(details.get('tags', []))

            markdown_content += f"## {summary}\n\n"
            markdown_content += f"**Método:** `{method.upper()}`\n"
            markdown_content += f"**Caminho:** `{path}`\n"
            if tags:
                markdown_content += f"**Tags:** {tags}\n"
            markdown_content += f"\n{description}\n\n"

            # Parâmetros
            parameters = details.get('parameters')
            if parameters:
                markdown_content += "### Parâmetros\n\n"
                markdown_content += "| Nome | Em | Tipo | Descrição | Obrigatório | Exemplo |\n"
                markdown_content += "|---|---|---|---|---|---|\n"
                for param in parameters:
                    name = param.get('name', 'N/A')
                    location = param.get('in', 'N/A')
                    param_type = param.get('schema', {}).get('type', 'N/A')
                    param_description = param.get('description', 'N/A').replace('\n', ' ')
                    required = "Sim" if param.get('required', False) else "Não"
                    example = param.get('schema', {}).get('example', 'N/A')
                    markdown_content += f"| `{name}` | `{location}` | `{param_type}` | {param_description} | {required} | `{example}` |\n"
                markdown_content += "\n"

            # Corpo da Requisição (Request Body)
            request_body = details.get('requestBody')
            if request_body:
                markdown_content += "### Corpo da Requisição\n\n"
                content = request_body.get('content', {})
                for media_type, media_details in content.items():
                    markdown_content += f"**Tipo de Conteúdo:** `{media_type}`\n\n"
                    schema = media_details.get('schema')
                    if schema:
                        example = media_details.get('example')
                        if example:
                            markdown_content += "**Exemplo de Requisição:**\n\n```json\n"
                            markdown_content += yaml.dump(example, indent=2, sort_keys=False) + "\n```\n\n"
                        
                        properties = schema.get('properties')
                        if properties:
                            required_props = schema.get('required', [])
                            
                            markdown_content += "**Propriedades:**\n\n"
                            markdown_content += format_schema_properties(properties, indent_level=0)
                            markdown_content += "\n"
                        
                        if 'items' in schema and schema['type'] == 'array':
                            markdown_content += "**Itens do Array:**\n\n"
                            items_schema = schema['items']
                            items_properties = items_schema.get('properties')
                            if items_properties:
                                markdown_content += format_schema_properties(items_properties, indent_level=0)
                                markdown_content += "\n"

            # Respostas
            responses = details.get('responses')
            if responses:
                markdown_content += "### Respostas\n\n"
                markdown_content += "| Código | Descrição | Esquema |\n"
                markdown_content += "|---|---|---|\n"
                for status_code, response_details in responses.items():
                    description = response_details.get('description', 'N/A').replace('\n', ' ')
                    content_schema = ""
                    if 'content' in response_details:
                        for media_type, media_details in response_details['content'].items():
                            if 'schema' in media_details:
                                if media_details['schema'].get('type') == 'string' and media_details['schema'].get('format') == 'binary':
                                    content_schema = f"`{media_type}` (binário)"
                                else:
                                    content_schema = f"`{media_type}`: `{media_details['schema'].get('type', 'object')}`"
                                    if 'properties' in media_details['schema']:
                                        content_schema += "\n\n**Propriedades da Resposta:**\n\n"
                                        content_schema += format_schema_properties(media_details['schema']['properties'], indent_level=1)
                                    if 'items' in media_details['schema'] and media_details['schema']['type'] == 'array':
                                        content_schema += "\n\n**Itens do Array da Resposta:**\n\n"
                                        if 'properties' in media_details['schema']['items']:
                                            content_schema += format_schema_properties(media_details['schema']['items']['properties'], indent_level=1)
                                        else:
                                            content_schema += f"    Tipo: `{media_details['schema']['items'].get('type', 'N/A')}`\n"


                    markdown_content += f"| `{status_code}` | {description} | {content_schema} |\n"
                markdown_content += "\n"
    return markdown_content

def update_mkdocs_nav(mkdocs_config_path, api_docs_subdir, generated_pages):
    """Atualiza a seção 'nav' do mkdocs.yml com as novas páginas da API."""
    try:
        with open(mkdocs_config_path, 'r', encoding='utf-8') as f:
            mkdocs_config = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{mkdocs_config_path}' não encontrado. Certifique-se de que está na raiz do seu projeto MkDocs.")
        return

    if 'nav' not in mkdocs_config:
        mkdocs_config['nav'] = []

    # Encontra ou cria a seção 'API Reference'
    api_reference_node = None
    for item in mkdocs_config['nav']:
        if isinstance(item, dict) and 'API Reference' in item:
            api_reference_node = item['API Reference']
            break
    
    if api_reference_node is None:
        api_reference_node = []
        mkdocs_config['nav'].append({'API Reference': api_reference_node})
    
    # Adiciona as novas páginas, garantindo que não haja duplicatas
    existing_api_pages = set()
    for item in api_reference_node:
        if isinstance(item, dict):
            existing_api_pages.add(list(item.values())[0]) # assumes format {'Title': 'path/to/file.md'}
        elif isinstance(item, str):
            existing_api_pages.add(item) # assumes format 'path/to/file.md'

    for title, path in sorted(generated_pages.items()):
        full_path = f"{api_docs_subdir}/{path}"
        # Verifica se a página já existe na navegação antes de adicionar
        if full_path not in existing_api_pages and {'API Reference': full_path} not in api_reference_node: # Check for both dict and string formats
            api_reference_node.append({title: full_path})

    with open(mkdocs_config_path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(mkdocs_config, f, sort_keys=False, default_flow_style=False, allow_unicode=True, indent=2)
    
    print(f"\nArquivo '{mkdocs_config_path}' atualizado com sucesso.")

# --- Lógica Principal ---

def main():
    print(f"Iniciando a geração da documentação da API a partir de '{SWAGGER_FILE_PATH}'...")

    # 1. Leitura e Parsing do Swagger
    try:
        with open(SWAGGER_FILE_PATH, 'r', encoding='utf-8') as f:
            swagger_content = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo Swagger '{SWAGGER_FILE_PATH}' não foi encontrado.")
        return
    except yaml.YAMLError as e:
        print(f"Erro ao parsear o arquivo Swagger YAML: {e}")
        return

    paths = swagger_content.get('paths', {})
    
    # Agrupar endpoints por x-api
    api_groups = defaultdict(lambda: defaultdict(dict))

    for path, path_details in paths.items():
        for method, method_details in path_details.items():
            if method.lower() in ['get', 'post', 'put', 'delete', 'patch']: # Apenas métodos HTTP
                x_api_value = method_details.get('x-api')
                if x_api_value:
                    api_groups[x_api_value][path][method] = method_details
                else:
                    # Opcional: lidar com endpoints sem x-api, talvez em uma página "General"
                    # api_groups['general'][path][method] = method_details
                    pass

    # Caminho completo para o diretório de destino dos arquivos Markdown
    full_api_docs_path = os.path.join(MKDOCS_DOCS_DIR, API_DOCS_SUBDIR)
    os.makedirs(full_api_docs_path, exist_ok=True)

    generated_pages = {} # { "Título da Página": "caminho/do/arquivo.md" }

    # 2. Geração de Arquivos Markdown
    print(f"\nGerando arquivos Markdown no diretório: '{full_api_docs_path}'...")
    for api_name, endpoints in api_groups.items():
        file_name = f"{sanitize_filename(api_name)}.md"
        file_path = os.path.join(full_api_docs_path, file_name)
        
        markdown_content = generate_markdown_content(api_name, endpoints)
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"  - '{file_name}' gerado com sucesso.")
            generated_pages[api_name.replace('-', ' ').title()] = file_name
        except IOError as e:
            print(f"Erro ao escrever o arquivo '{file_path}': {e}")

    # 3. Atualização do mkdocs.yml
    mkdocs_config_full_path = os.path.join('.', MKDOCS_CONFIG_FILE) # Assume mkdocs.yml na raiz do projeto
    update_mkdocs_nav(mkdocs_config_full_path, API_DOCS_SUBDIR, generated_pages)
    
    print("\nProcesso de geração da documentação da API concluído!")
    print(f"Lembre-se de rodar 'mkdocs serve' ou 'mkdocs build' para ver as mudanças.")

if __name__ == "__main__":
    main()