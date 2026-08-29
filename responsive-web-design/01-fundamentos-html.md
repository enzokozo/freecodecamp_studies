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

## 5. Elementos `<div>` e Agrupamento de Conteúdo

A tag `<div>` (abreviação de *division* ou divisão) é um dos elementos mais utilizados no HTML. Ela funciona como um **contêiner genérico** para agrupar outros elementos.

* **Sem significado semântico:** Diferente de tags como `<h1>` (que indica um título importante) ou `<p>` (que indica um parágrafo), a `<div>` não diz nada ao navegador ou aos leitores de tela sobre o tipo de conteúdo que ela guarda. Ela não tem valor visual pré-definido (é "invisível" até você estilizá-la).
* **Propósito principal:** O verdadeiro poder da `<div>` aparece quando precisamos agrupar elementos relacionados para estilizá-los em conjunto usando CSS (geralmente aplicando atributos como `class` ou `id`) ou para manipulá-los com JavaScript.
* **Nível de Bloco (*Block-level*):** Por padrão, uma `<div>` ocupa 100% da largura disponível, forçando o elemento seguinte a ir para a próxima linha (como se fosse um bloco retangular invisível na página).

### Como usar a `<div>`

Pense nela como uma "caixa" onde você organiza outros itens. No exemplo abaixo, agrupamos uma imagem, um título e um parágrafo dentro de uma mesma "caixa" que representa o perfil de um usuário:

```html
<div class="perfil-usuario">
  <img src="foto.jpg" alt="Foto de perfil">
  <h2>Maria Souza</h2>
  <p>Desenvolvedora Front-end</p>
</div>
```

---
> **💡 Dicas:** 
> Cuidado com a doença crônica do desenvolvedor iniciante: a "Divite" (*Divitis*), que é o vício de embrulhar tudo em `<div>`! Embora as divs sejam indispensáveis, o HTML moderno possui **tags semânticas** (como `<header>`, `<footer>`, `<main>`, `<section>` e `<article>`). Sempre que o seu bloco de conteúdo tiver uma função clara (ex: o rodapé da página ou um artigo de blog), prefira a tag semântica no lugar de uma `<div>` genérica. Isso melhora o SEO (ranqueamento no Google) e a acessibilidade para pessoas que usam leitores de tela.

## 6. Identificadores: Atributos `id` e `class`

Os atributos `id` e `class` são "atributos globais" (podem ser usados em quase qualquer tag) fundamentais no HTML. Eles servem como "etiquetas" que damos aos nossos elementos para que o CSS (estilos) e o JavaScript (interações) saibam exatamente com qual tag estão lidando.

Embora pareçam ter a mesma função, a diferença entre eles é de extrema importância:

*   **O atributo `id` (Identidade Única):** Funciona como o CPF do elemento. O valor de um `id` deve ser **estritamente único** dentro de um mesmo documento HTML. Você nunca deve ter dois elementos com o mesmo `id` na mesma página.
    *   *Uso comum:* Identificar seções únicas da página (ex: o cabeçalho principal), servir como âncora para links internos (rolar a página até aquele ponto) ou como um alvo rápido para o JavaScript.

*   **O atributo `class` (Classe ou Grupo):** Funciona como um uniforme de time. Você pode dar a **mesma** `class` para quantos elementos quiser na sua página.
    *   *Uso comum:* Agrupar elementos que vão compartilhar o mesmo visual (ex: vários botões que precisam ter a mesma cor, fonte e tamanho).

### Como aplicar no HTML

No exemplo abaixo, usamos um `id` para a barra de navegação (já que só existe uma principal) e uma `class` para os botões (já que são vários e compartilham o mesmo padrão visual):

```html
<div id="navegacao-principal">
  <button class="botao-padrao">Início</button>
  <button class="botao-padrao">Sobre</button>
  <button class="botao-padrao">Contato</button>
</div>
```

---
> **💡 Dicas:** 
> 1. **Múltiplas classes:** Um único elemento pode ter várias classes ao mesmo tempo. Basta separá-las por espaço na declaração (ex: `<div class="caixa destaque fundo-escuro">`).
> 2. **Regra de Ouro do Mercado:** Na hora de aplicar regras visuais no CSS, prefira **sempre** usar o atributo `class`. Estilizar elementos pelo `id` deixa o seu CSS muito "engessado" (vamos aprender sobre *especificidade* do CSS no futuro) e dificulta a reutilização do código. Guarde os `id`s para interações com JavaScript, para formulários (ligar um `<label>` a um `<input>`) ou para links internos.

## 7. Entidades HTML (HTML Entities)

Em HTML, alguns caracteres são "reservados". Por exemplo, os sinais de menor que (`<`) e maior que (`>`) são usados para criar as tags. Se você tentar simplesmente digitar "2 < 5" ou quiser exibir o texto "&lt;h1&gt;" na tela, o navegador vai se confundir, achando que você está tentando abrir uma nova tag, e o layout da página pode quebrar. 

Para resolver isso, usamos as **Entidades HTML** (*HTML Entities*).

* **O que são:** São códigos de texto curtos usados para exibir caracteres reservados pelo HTML, símbolos invisíveis, ou ícones que não estão facilmente disponíveis no teclado (como ©, ™, ou setas).
* **Sintaxe padrão:** Toda entidade começa com um "e comercial" (`&`), seguido pelo nome da entidade (ou um número de identificação), e termina obrigatoriamente com um ponto e vírgula (`;`).

### Entidades mais comuns no dia a dia:

*   `&lt;` (*less than*): Renderiza o sinal de menor `<`
*   `&gt;` (*greater than*): Renderiza o sinal de maior `>`
*   `&amp;` (*ampersand*): Renderiza o "e comercial" `&`
*   `&copy;`: Renderiza o símbolo de copyright `©`
*   `&nbsp;` (*non-breaking space*): Renderiza um espaço em branco "inquebrável".

### Como aplicar no HTML

No exemplo abaixo, usamos entidades para mostrar a sintaxe de uma tag sem que o navegador tente executá-la, e depois usamos para exibir um símbolo de direitos autorais no rodapé:

```html
<p>Para criar um título principal no HTML, nós usamos a tag &lt;h1&gt;.</p>

<footer>
  <p>FreeCodeCamp &copy; 2026</p>
</footer>
```

---
> **💡 Dicas:** 
> A entidade `&nbsp;` (*Non-Breaking Space*) é uma carta na manga excelente. Ela cria um espaço entre duas palavras, mas "amarra" as duas juntas. Isso impede que o navegador separe essas palavras em linhas diferentes quando o espaço da tela fica apertado (em celulares, por exemplo). É uma excelente prática de tipografia usar isso entre um valor e sua unidade de medida, como em `10&nbsp;kg` ou `R$&nbsp;50,00`, garantindo que o número e o símbolo fiquem sempre na mesma linha.

## 8. O Elemento `<script>` e a Inclusão de JavaScript

Se o HTML é o esqueleto da sua página e o CSS (trazido pela tag `<link>`) é a aparência, o JavaScript é o "músculo" ou o "cérebro" que permite a interatividade. Para conectar códigos de programação ao seu HTML, usamos o elemento `<script>`.

* **Objetivo:** Inserir ou referenciar códigos executáveis, quase sempre JavaScript, no documento HTML.
* **Não é uma tag vazia:** Ao contrário da tag `<link>` ou `<img>`, o elemento `<script>` **sempre** precisa de uma tag de fechamento `</script>`, mesmo quando você está apenas conectando um arquivo externo.

### Como usar o `<script>`

Existem duas abordagens para usar essa tag, de forma bem similar ao que fazemos com o CSS:

**1. Código Interno (Inline):**
Você pode escrever o código de programação diretamente entre as tags de abertura e fechamento. Isso é útil apenas para scripts minúsculos ou testes rápidos.

```html
<script>
  console.log("Olá! Este texto vai aparecer no console do navegador.");
</script>
```

**2. Código Externo (A Melhor Prática):**
Em projetos reais, separamos as linguagens em arquivos diferentes. Para conectar um arquivo JavaScript externo, usamos o atributo `src` (*source*, ou fonte) apontando para o arquivo `.js`.

```html
<!-- Conectando um arquivo externo chamado "app.js" -->
<script src="app.js"></script>
```

---
> **💡 Dicas:** 
> O local onde você coloca o `<script>` no seu documento impacta diretamente na performance (tempo de carregamento) do seu site. O comportamento padrão do navegador é pausar a leitura do HTML, baixar o script, executá-lo e só então voltar a ler o HTML. 
>
> Se o seu JavaScript for pesado e estiver no topo (`<head>`), a tela do usuário ficará em branco travada até o download terminar. 
>
> **A solução moderna:** Coloque o `<script>` no `<head>` e adicione o atributo `defer`.
> Exemplo: `<script src="app.js" defer></script>`. O `defer` avisa ao navegador: *"Pode ir baixando o script nos bastidores, mas só o execute quando a página inteira estiver desenhada na tela."* Isso garante um carregamento muito mais rápido para o usuário.

## 9. A Tag Meta Description e seu Papel no SEO

A tag `<meta>` possui várias funções de configuração dentro do `<head>` do seu documento. Quando a utilizamos com o atributo `name="description"`, ela assume um papel vital para o **SEO** (*Search Engine Optimization* ou Otimização para Mecanismos de Busca).

* **O que é:** É um breve resumo do conteúdo da sua página web. 
* **Para que serve:** Os mecanismos de busca (como o Google) geralmente exibem esse texto na página de resultados (SERP) logo abaixo do título azul clicável e da URL do site.
* **Como afeta o SEO:** O Google já declarou que a *meta description* não é um fator direto para subir posições no ranking. No entanto, ela é a principal responsável por gerar interesse e convencer o usuário a clicar no seu link em vez de clicar no link do concorrente.

### Como aplicar no HTML

A declaração exige dois atributos trabalhando em conjunto: o `name="description"` (que avisa à máquina qual é o propósito desta tag específica) e o `content` (que guarda o texto do seu resumo).

```html
<head>
  <meta charset="utf-8">
  <title>Aprenda a Programar</title>
  <!-- Exemplo de Meta Description -->
  <meta name="description" content="Aprenda desenvolvimento web do zero com tutoriais práticos de HTML, CSS e JavaScript. Comece sua carreira na tecnologia hoje!">
</head>
```

---
> **💡 Dicas:** 
> O tamanho do texto que você escreve no atributo `content` importa muito. Se for muito longo, o Google simplesmente vai cortar a sua frase e colocar reticências (`...`) no final, o que parece pouco profissional. A recomendação padrão do mercado é manter a sua *meta description* entre **150 e 160 caracteres**. Pense nesse texto como o "pitch de vendas" da sua página: seja claro, honesto sobre o conteúdo e escreva um texto convidativo.

## 10. Tags Open Graph (OG) e Compartilhamento em Redes Sociais

Você já reparou que, quando você envia um link no WhatsApp, LinkedIn, Discord ou Twitter, o aplicativo automaticamente gera um "cartão" bonito (chamado de *Rich Card*) com uma imagem de capa, um título chamativo e um resumo? Quem controla exatamente o que aparece nesse cartão são as **Tags Open Graph**.

* **O que são:** É um protocolo criado originalmente pelo Facebook, mas que se tornou o padrão da indústria, usado para controlar como uma página da web é apresentada quando compartilhada em redes sociais.
* **Como funciona:** Elas são tags `<meta>` adicionadas ao `<head>` do seu documento. Em vez do atributo `name` tradicional (como vimos na *meta description*), o padrão Open Graph utiliza o atributo `property` com valores que sempre começam com o prefixo `og:`.

### Principais Tags Open Graph

* `og:title`: O título da sua página (como você quer que apareça na rede social).
* `og:description`: Um breve resumo (geralmente parecido com a sua *meta description*).
* `og:image`: O link direto para a imagem de capa que vai aparecer no cartão.
* `og:url`: O endereço oficial da página.
* `og:type`: O tipo de conteúdo (geralmente `website` ou `article`).

### Como aplicar no HTML

```html
<head>
  <!-- Outras configurações do head... -->
  
  <!-- Configurações Open Graph -->
  <meta property="og:title" content="Aprenda a Programar do Zero">
  <meta property="og:description" content="Curso prático de HTML e CSS.">
  <meta property="og:image" content="https://seusite.com/imagens/capa.jpg">
  <meta property="og:url" content="https://seusite.com/curso">
  <meta property="og:type" content="website">
</head>
```

---
> **💡 Dicas:** 
> 1. **A imagem é crucial:** A tag `og:image` é o que mais atrai cliques. O padrão da indústria para garantir que a imagem não fique cortada nem esticada nas redes sociais é usar o tamanho de **1200 x 630 pixels**. E lembre-se: o caminho na tag `content` da imagem deve ser o link absoluto e completo (começando com `https://`), não o caminho local do seu computador.
> 2. **X (antigo Twitter):** O Twitter tem as suas próprias meta tags (ex: `<meta name="twitter:card" content="summary_large_image">`), mas como medida de segurança, se ele não encontrar as tags do Twitter, ele usa as tags Open Graph como plano B. Portanto, garantir o Open Graph resolve 90% do seu problema de compartilhamento.

## 11. Elementos `<audio>` e `<video>`

Antigamente, para tocar uma música ou exibir um vídeo em um site, os desenvolvedores dependiam de plugins externos pesados e cheios de falhas de segurança, como o Adobe Flash Player. O HTML5 resolveu isso introduzindo tags nativas e semânticas para lidar com mídia: `<audio>` e `<video>`.

* **Como funcionam:** Ambas as tags possuem uma estrutura quase idêntica. Elas atuam como um contêiner (*wrapper*) para os arquivos de mídia.
* **A tag `<source>`:** Embora você possa usar o atributo `src` direto na tag de áudio/vídeo, a melhor prática é usar a tag `<source>` dentro delas. Ela é *self-closing* (vazia) e permite que você ofereça o mesmo arquivo em diferentes formatos. O navegador vai ler a lista de cima para baixo e tocar o primeiro formato que ele for capaz de rodar.
* **Texto de *Fallback* (Reserva):** O texto que você coloca entre a tag de abertura e fechamento só será exibido na tela se o navegador do usuário for muito antigo e não suportar aquele elemento.

### Principais Atributos:

Para essas tags serem úteis, elas dependem de alguns atributos específicos (a maioria deles não precisa do sinal de igual, basta declarar o nome):

* `controls`: O mais importante. Mostra os controles nativos do navegador (botão de play/pause, barra de progresso, volume e tela cheia).
* `autoplay`: Faz a mídia começar a tocar automaticamente assim que a página carrega.
* `loop`: Faz o áudio ou vídeo recomeçar sozinho quando chega ao fim.
* `muted`: Inicia a mídia sem som.

### Como aplicar no HTML

```html
<!-- Exemplo de Vídeo -->
<video controls width="600">
  <!-- O navegador tentará rodar o mp4; se não conseguir, tenta o webm -->
  <source src="apresentacao.mp4" type="video/mp4">
  <source src="apresentacao.webm" type="video/webm">
  Desculpe, o seu navegador não suporta a exibição de vídeos.
</video>

<!-- Exemplo de Áudio -->
<audio controls>
  <source src="podcast.mp3" type="audio/mpeg">
  Desculpe, o seu navegador não suporta a tag de áudio.
</audio>
```

---
> **💡 Dicas:** 
> O maior erro de UX (Experiência do Usuário) que um desenvolvedor pode cometer é usar o atributo `autoplay` tocando som sem a permissão do usuário. Ninguém gosta de entrar em um site e levar um susto com um vídeo alto. 
> 
> Inclusive, os navegadores modernos (como Chrome e Safari) hoje em dia **bloqueiam** automaticamente qualquer `autoplay` que tenha som. Se você realmente precisa que um vídeo inicie sozinho no fundo da tela, você é obrigado a usar `autoplay` e `muted` juntos (ex: `<video autoplay muted loop>`).