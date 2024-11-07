import re

# Definição de palavras-chave em Java
PALAVRAS_CHAVE = [
    "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", 
    "const", "continue", "default", "do", "double", "else", "enum", "extends", 
    "final", "finally", "float", "for", "goto", "if", "implements", "import", "instanceof", 
    "int", "interface", "long", "native", "new", "package", "private", "protected", 
    "public", "return", "short", "static", "strictfp", "super", "switch", "synchronized", 
    "this", "throw", "throws", "transient", "try", "void", "volatile", "while"
]

# Definição de operadores aritméticos em Java
OPERADORES_ARITMETICOS = [
    "+", "-", "*", "/", "++", "--", "+=", "-=", "*=", "/=", "%="
]

# Definição de operadores lógicos em Java
OPERADORES_LOGICOS = [
    "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", ">>>"
]

# Definição de delimitadores (parênteses, chaves, vírgulas, ponto e vírgula e dois pontos)
DELIMITADORES = [
    "(", ")", "{", "}", ",", ";", ":"
]

# Definição de tipos de dados em Java
TIPOS_DADOS = ["int", "float", "double", "boolean", "char", "byte", "short", "long", "void"]

# Expressões regulares para identificar tokens
EXPRESSOES_REGULARES = {
    'palavra_chave': r'\b(?:' + '|'.join(PALAVRAS_CHAVE) + r')\b',
    'identificador': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'numero': r'\b\d+(\.\d+)?\b',
    'string': r'"[^"]*"',  # Captura strings entre aspas
    'operador_aritmetico': r'|'.join(re.escape(op) for op in OPERADORES_ARITMETICOS),
    'operador_logico': r'|'.join(re.escape(op) for op in OPERADORES_LOGICOS),
    'delimitador': r'|'.join(re.escape(d) for d in DELIMITADORES)
}

# Combinação de todas as expressões regulares para tokenização
PADRAO_GERAL = r'|'.join(f'(?P<{tipo}>{padrao})' for tipo, padrao in EXPRESSOES_REGULARES.items())

# Função para tokenizar uma linha de código sem duplicação
def tokenizar_linha_sem_duplicacao(linha):
    tokens = []
    for match in re.finditer(PADRAO_GERAL, linha):
        tipo_token = match.lastgroup
        token = match.group(tipo_token)
        if tipo_token == 'string':
            conteudo_string = token.strip('"')
            elementos = re.findall(r'\w+|[^\w\s]', conteudo_string)
            for elemento in elementos:
                tokens.append((elemento, 'identificador'))
        else:
            tokens.append((token, tipo_token))
    return tokens

# Função principal para processar o arquivo Java e gerar a tabela de tokens e símbolos
def analisar_arquivo_java(caminho_arquivo):
    tabela_tokens = []
    tabela_simbolos = {}
    tipo_atual = None
    contador_identificador = 1

    with open(caminho_arquivo, 'r') as arquivo:
        for num_linha, linha in enumerate(arquivo, 1):
            tokens = tokenizar_linha_sem_duplicacao(linha)
            for token, tipo_token in tokens:
                tabela_tokens.append((token, tipo_token, num_linha))

                if tipo_token == 'palavra_chave' and token in TIPOS_DADOS:
                    tipo_atual = token
                elif tipo_token == 'identificador':
                    if token not in tabela_simbolos:
                        tabela_simbolos[token] = {
                            'linhas': [num_linha],
                            'tipo': f'identificador_{contador_identificador}'
                        }
                        contador_identificador += 1
                    else:
                        tabela_simbolos[token]['linhas'].append(num_linha)
                    tipo_atual = None

    return tabela_tokens, tabela_simbolos

# Função para exibir as tabelas com formatação adaptativa
def exibir_tabelas_adaptativas(tabela_tokens, tabela_simbolos):
    # Calcular largura das colunas para a tabela de tokens
    largura_token = max(len(str(token)) for token, _, _ in tabela_tokens) + 2
    largura_tipo = max(len(str(tipo)) for _, tipo, _ in tabela_tokens) + 2
    largura_linha = max(len(str(linha)) for _, _, linha in tabela_tokens) + 2
    largura_total_tokens = largura_token + largura_tipo + largura_linha + 10

    print("-" * largura_total_tokens)
    print(f"| {'Tabela de Tokens:':^{largura_total_tokens - 2}} |")
    print("-" * largura_total_tokens)
    for token, tipo_token, linha in tabela_tokens:
        print(f'|Token: {token:<{largura_token}}| Tipo: {tipo_token:<{largura_tipo}}| Linha: {linha:<{largura_linha}}|')
    print("-" * largura_total_tokens)

    # Calcular largura das colunas para a tabela de símbolos
    largura_simbolo = max(len(simbolo) for simbolo in tabela_simbolos) + 2
    largura_linhas = max(len(", ".join(map(str, detalhes['linhas']))) for detalhes in tabela_simbolos.values()) + 2
    largura_tipo = max(len(detalhes['tipo']) for detalhes in tabela_simbolos.values()) + 2
    largura_total_simbolos = largura_simbolo + largura_linhas + largura_tipo + 10

    print("-" * largura_total_simbolos)
    print(f"| {'Tabela de Símbolos:':^{largura_total_simbolos - 2}} |")
    print("-" * largura_total_simbolos)
    for simbolo, detalhes in tabela_simbolos.items():
        linhas = ", ".join(map(str, detalhes['linhas']))
        print(f"| Símbolo: {simbolo:<{largura_simbolo}}| Linhas: {linhas:<{largura_linhas}}| Tipo: {detalhes['tipo']:<{largura_tipo}} |")
    print("-" * largura_total_simbolos)

# Exemplo de uso
caminho_arquivo = "base.java"
tabela_tokens, tabela_simbolos = analisar_arquivo_java(caminho_arquivo)

# Exibir as tabelas de forma adaptativa
exibir_tabelas_adaptativas(tabela_tokens, tabela_simbolos)
