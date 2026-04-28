# 📸 Smile Selfie — Detecção de Sorriso com Python e OpenCV

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

 o programa detecta **rostos e sorrisos em tempo real** via câmera do celular (DroidCam ou Iriun Webcam) e só tira a foto quando você **está sorrindo e pressiona `C`** — sem fotos indesejadas!

---

## Como funciona

```
[Câmera do Celular]  →  [OpenCV: Haar Cascade]  →  [Detecta rosto + sorriso]
                                                          ↓
                                               Pressione C para capturar
                                                          ↓
                                         📁 sorriso_20250428_153045.jpg
```

---

## Funcionalidades

| Recurso | Detalhe |

|  Câmera via USB ou Wi-Fi | Compatível com DroidCam e Iriun Webcam |
| Detecção de rosto | Retângulo azul ao redor do rosto |
| Detecção de sorriso | Retângulo verde dentro da região do rosto |
|  Feedback visual | Mensagem na tela indicando se o sorriso está ativo |
|  Captura inteligente | Foto só é tirada ao sorrir **+** pressionar `C` |
|  Arquivo salvo com timestamp: `sorriso_YYYYMMDD_HHMMSS.jpg` 
|   Pressione `Q` para encerrar a qualquer momento 

---

## Estrutura do Projeto

```
smile-selfie/
├── smile_selfie.py       # Script principal
├── requirements.txt      # Dependências
├── README.md
└── fotos/                # Pasta criada automaticamente para as selfies
```


### Aplicativos de câmera para celular (opcional)

| App | Conexão | Link |
|---|---|---|
| [DroidCam](https://www.dev47apps.com/) | USB ou Wi-Fi | Android / iOS |
| [Iriun Webcam](https://iriun.com/) | USB ou Wi-Fi | Android / iOS |

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/smile-selfie.git
cd smile-selfie
```

### 2. (Recomendado) Crie um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> **`requirements.txt`**
> ```
> opencv-python
> numpy
> ```

---

## Como usar

### Execute o script

```bash
python smile_selfie.py
```

### Controles

| Tecla | Ação |
|---|---|
| `C` | 📸 Captura a foto *(somente se sorrindo)* |
| `Q` | ❌ Encerra o programa |



## Onde as fotos são salvas?

As fotos são salvas automaticamente na pasta do script com o formato:

```
sorriso_20250428_153045.jpg
```

---

## Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/) — visão computacional e classificadores Haar Cascade
- [NumPy](https://numpy.org/) — processamento de arrays de imagem
- [DroidCam](https://www.dev47apps.com/) / [Iriun Webcam](https://iriun.com/) — câmera via celular

---





> Feito com 😄 e Python
