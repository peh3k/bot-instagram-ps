# Bot Instagram PS

![GitHub language count](https://img.shields.io/github/languages/count/peh3k/conversor-de-bases-numericas?style=for-the-badge)

> Esse é um **Bot** para **Instagram**, que usa um sistema que eu chamo de *PS* - **perceive** and **send** (perceber e enviar), como o próprio nome já diz, ele é capaz de **receber** e **enviar** mensagens no direct com uma mensagem pré selecionada.

## Bibliotecas utilizadas

- `<Selenium>`
- `<PySimpleGui>`

### Ajustes e melhorias

O projeto ainda está em **desenvolvimento** e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Salvar credenciais de Login
- [x] Login automático
- [x] Responder a partir do direct principal
- [ ] Responder a partir das solicitações
- [ ] Chat Bot completo

## 💻 Pré-requisitos

Antes de começar, **verifique** se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Possuir a versão mais recente de `<Python>` em sua máquina
* Possuir `<PyCharm / VsCode / Outros>`




## 🚀 Instalando PySimpleGui

Para instalar o *PySimpleGui*, siga estas etapas:

**Linux:**
```
pip install pysimplegui
```

**Windows:**
```
pip install pysimplegui
```
## 🚀 Instalando Selenium

Para instalar o *Selenium*, siga estas etapas:

**Linux:**
```
pip install selenium
```

**Windows:**
```
pip install selenium
```
## 🚀 Instalando WebDriver Chrome

Para instalar o *WebDriver* do Chrome, siga estas etapas:

- Baixe o arquivo <a href="https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/install_drivers/">WebDriver Chrome</a>
- Extraia os arquivos

**Linux:**

  Dentro da mesma pasta do arquivo digite o comando:

```
sudo mv chomedriver /usr/local/bin/
```
**Windows:**

- Crie uma pasta
- Mova o arquivo "chromedriver.exe" para esta pasta
- Inicie o VsCode nesta mesma pasta
- Na linha 93 do código modifique de:
```
self.pagina = webdriver.Chrome()
```
para:
```
self.pagina = webdriver.Chrome('./chromedriver.exe')
```
Pronto agora é só rodar



## ❗ Observações Importantes ❗
- Baixe as *imagens* e o arquivo '*usr.txt*' e os coloque em uma pasta
- Rode o código dentro dessa mesma pasta
- Sem as *imagens* e o arquivo *txt* o programa **não** funciona!
- Algum *Bug* pode ocorrer, portanto, me **notifique!**

### Author <a href="https://github.com/peh3k">peh3k</a>

[⬆ Voltar ao topo](#conversor-de-bases-numericas)<br>

