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

# Definição de delimitadores (parênteses, chaves e vírgulas)
DELIMITADORES = [
    "(", ")", "{", "}", ","
]

# Definição de tipos de dados em Java
TIPOS_DADOS = ["int", "float", "double", "boolean", "char", "byte", "short", "long", "void"]

# Expressões regulares para identificar tokens
EXPRESSOES_REGULARES = {
    'palavra_chave': r'\b(?:' + '|'.join(PALAVRAS_CHAVE) + r')\b',
    'identificador': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'numero': r'\b\d+(\.\d+)?\b',
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
        tokens.append((token, tipo_token))
    
    return tokens

# Função principal para processar o arquivo Java e gerar a tabela de tokens e símbolos
def analisar_arquivo_java(caminho_arquivo):
    tabela_tokens = []
    tabela_simbolos = {}
    tipo_atual = None  # Para armazenar o tipo atual enquanto processamos a linha

    with open(caminho_arquivo, 'r') as arquivo:
        for num_linha, linha in enumerate(arquivo, 1):  # Adicionando número da linha para a tabela de símbolos
            tokens = tokenizar_linha_sem_duplicacao(linha)
            for token, tipo_token in tokens:
                # Evitar duplicação de tokens na tabela de tokens
                if (token, tipo_token) not in tabela_tokens:
                    tabela_tokens.append((token, tipo_token))
                
                # Verifica se o token atual é um tipo de dado
                if tipo_token == 'palavra_chave' and token in TIPOS_DADOS:
                    tipo_atual = token  # Define o tipo atual
                elif tipo_token == 'identificador':
                    # Se for identificador e há um tipo de dado associado, atualiza a tabela de símbolos
                    if token not in tabela_simbolos:
                        tabela_simbolos[token] = {'linha': num_linha, 'tipo': tipo_atual or 'desconhecido'}
                    tipo_atual = None  # Redefine o tipo após associar a um identificador
    
    return tabela_tokens, tabela_simbolos

# Exemplo de uso
caminho_arquivo = "arquivo.java"
tabela_tokens, tabela_simbolos = analisar_arquivo_java(caminho_arquivo)

# Exibir a tabela de tokens
print("-" * 70)
print(f"| {'Tabela de Tokens:':<66} |")
print("-" * 70)
for token, tipo_token in tabela_tokens:
    print(f'|Token: {token:<20}| Tipo: {tipo_token:<33}|')
print("-" * 70)
print(" " * 70)

# Exibir a tabela de símbolos
print("-" * 70)
print(f"| {'Tabela de Símbolos:':<66} |")
print("-" * 70)
for simbolo, detalhes in tabela_simbolos.items():
    print(f"| Símbolo: {simbolo:<10}| Linha: {detalhes['linha']:<10}| Tipo: {detalhes['tipo']:<20} |")  
print("-" * 70)