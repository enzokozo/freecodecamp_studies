# Módulo 1: Fundamentos de HTML

## 1. O que é HTML e Elementos Básicos
HTML (*HyperText Markup Language*) é uma **linguagem de marcação** (não de programação) usada para estruturar e exibir conteúdo na web. O HTML utiliza "tags" para classificar diferentes partes do conteúdo.

* **Sintaxe padrão:** Um elemento é formado por uma tag de abertura, o conteúdo e uma tag de fechamento. 
  * Exemplo: `<p>Este é um parágrafo.</p>`
* **Tags vazias (*self-closing*):** Não envolvem conteúdo de texto e não precisam de fechamento, como `<img>` para imagens ou `<br>` para quebras de linha.

## 2. Atributos HTML
Atributos são configurações extras aplicadas a um elemento HTML. Eles modificam o comportamento padrão da tag ou fornecem informações adicionais necessárias para que ela funcione.

* **Regras Fundamentais:**
  1. Os atributos são **sempre** declarados dentro da **tag de abertura**.
  2. Eles funcionam em pares, usando o formato: `nome="valor"`.

* **Categorias de Atributos:**
  * **Atributos Globais:** Podem ser usados em quase todas as tags.
    * `id="unico"`: Identificador único na página.
    * `class="grupo"`: Atribui uma classe (reutilizável em múltiplos elementos).
  * **Atributos Específicos:**
    * `href="url"`: Em tags `<a>`, define o destino do link.
    * `src="arquivo.jpg"`: Em tags `<img>`, aponta o caminho da imagem.
    * `alt="descrição"`: Em tags `<img>`, descreve a imagem (acessibilidade).

## 3. O Elemento `<link>` e Recursos Externos
Enquanto tags como `<p>` ou `<h1>` estruturam o conteúdo visual na tela, a tag `<link>` tem um propósito diferente: ela é usada para **conectar o documento HTML a recursos externos**.

* **Onde vai?** A tag `<link>` é quase sempre colocada dentro da seção `<head>` do seu documento (a parte invisível da página que guarda as configurações).
* **É vazia:** A tag `<link>` é *self-closing*, ou seja, não tem tag de fechamento.

### Atributos fundamentais do `<link>`:
Para a tag `<link>` funcionar, ela depende obrigatoriamente de dois atributos específicos:

1. **`rel` (Relacionamento):** Define qual é a relação do arquivo que estamos conectando com o nosso HTML atual. 
2. **`href` (Referência):** Indica o caminho ou a URL onde esse arquivo externo está guardado.

### O Uso Principal (Conectar CSS):
O caso de uso mais comum e importante para o `<link>` é conectar sua folha de estilos CSS para dar visual à página.

```html
<head>
  <!-- Conectando um arquivo CSS externo chamado "estilos.css" -->
  <link rel="stylesheet" href="estilos.css">
</head>
```

*Neste caso, o atributo `rel="stylesheet"` diz ao navegador: "Vá no caminho indicado no `href` e carregue as regras visuais que estão lá."*

### Outro Uso (Ícones da aba):
Você também usa a tag `<link>` para definir aquele pequeno ícone que aparece na aba do navegador (conhecido como *favicon*):

```html
<link rel="icon" type="image/png" href="icone.png">
```

💡**Dicas**:
Uma confusão comum no início é misturar as tags ```<a>``` (âncora) e ```<link>```. Pense assim:

* Você usa a tag ```<a>``` dentro do ```<body>``` para criar links clicáveis que o usuário vai acessar para navegar para outra página.

* Você usa a tag ```<link>``` dentro do ```<head>``` para a máquina (o navegador) buscar arquivos ocultos (como CSS ou fontes) necessários para montar a página atual.


## 4. Codificação de Caracteres (Character Encoding) e UTF-8

Assim como a tag `<link>` é usada para conectar arquivos, nós usamos a tag `<meta>` dentro do `<head>` para fornecer "metadados" (informações sobre a página) ao navegador. 

A configuração de metadados mais fundamental é definir como os textos da página devem ser lidos pelo computador, e isso é feito escolhendo a **codificação de caracteres**.

* **O problema:** Computadores leem números, não letras. Uma codificação de caracteres é uma tabela de tradução que diz ao computador qual número representa qual letra ou símbolo (ex: "o número 65 é a letra 'A'").
* **A solução (UTF-8):** Antigamente, havia várias tabelas de tradução, o que fazia sites estrangeiros aparecerem cheios de símbolos estranhos (como losangos pretos com interrogação). O **UTF-8** (*Unicode Transformation Format - 8-bit*) foi criado para unificar isso. Ele é capaz de traduzir praticamente qualquer caractere do mundo (incluindo letras acentuadas, alfabetos asiáticos e até emojis).

### Como configurar no HTML

Para garantir que o navegador exiba todos os textos (incluindo o "ç" e acentos do português) corretamente, você deve declarar o UTF-8 como a codificação padrão logo no início do `<head>` usando a tag `<meta>`.

```html
<head>
  <meta charset="utf-8">
</head>
```

* **`charset`:** É a abreviação de *character set* (conjunto de caracteres). É o atributo que define qual tabela de tradução o navegador deve usar.

---
> **💡 Dicas:** 
> Declare a tag `<meta charset="utf-8">` como o **primeiro** elemento dentro do seu `<head>`. Se o navegador começar a ler o documento, encontrar um texto com acento e só descobrir depois que a codificação era UTF-8, ele pode renderizar os caracteres incorretamente. Colocar essa tag no topo evita problemas de exibição logo de cara.