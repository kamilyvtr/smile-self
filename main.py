import cv2
import numpy as np
import os
import time
import glob

# ================== CONFIGURAÇÃO INICIAL ==================
base_dir = os.path.dirname(os.path.abspath(__file__))

xml_files = glob.glob(os.path.join(base_dir, "*.xml"))
if len(xml_files) < 2:
    print(f"ERRO: Encontrados apenas {len(xml_files)} arquivos .xml na pasta. Precisamos de 2.")
    print("Arquivos encontrados:", xml_files)
    exit()

face_xml = None
smile_xml = None
for f in xml_files:
    if 'face' in f.lower() or 'frontal' in f.lower():
        face_xml = f
    elif 'smile' in f.lower():
        smile_xml = f

if face_xml is None or smile_xml is None:
    print("Não foi possível identificar os classificadores. Verifique os nomes dos arquivos .xml")
    print("Arquivos:", xml_files)
    exit()

print(f"Carregando classificador de rosto: {os.path.basename(face_xml)}")
print(f"Carregando classificador de sorriso: {os.path.basename(smile_xml)}")

face_cascade = cv2.CascadeClassifier(face_xml)
smile_cascade = cv2.CascadeClassifier(smile_xml)

if face_cascade.empty():
    print("Erro: Não foi possível carregar o classificador de rosto.")
    exit()
if smile_cascade.empty():
    print("Erro: Não foi possível carregar o classificador de sorriso.")
    exit()

# ================== CONEXÃO COM A CÂMERA ==================
# Tenta abrir a câmera no índice 0 (webcam comum) ou 1 (DroidCam USB)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Câmera no índice 0 não funcionou. Tentando índice 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Erro: Não foi possível abrir nenhuma câmera. Verifique se o DroidCam Client está rodando e conectado via USB.")
    exit()

print("Câmera conectada. Comandos: 'c' para tirar foto (apenas se sorrindo), 'q' para sair.")

# ================== LOOP PRINCIPAL ==================
while True:
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar frame. Verifique a conexão da câmera.")
        break

    # Converte para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    sorriso_detectado = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        if len(smiles) > 0:
            sorriso_detectado = True
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
            cv2.putText(frame, "Sorriso detectado! Pressione 'c'", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Nenhum sorriso. Sorria!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    if len(faces) == 0:
        cv2.putText(frame, "Nenhum rosto detectado", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Smile Selfie - Pressione 'c' (sorriso) ou 'q'", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        if sorriso_detectado:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"sorriso_{timestamp}.jpg"
            filepath = os.path.join(base_dir, filename)
            cv2.imwrite(filepath, frame)
            print(f"📸 Foto salva: {filename}")
            cv2.putText(frame, "FOTO SALVA!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            cv2.imshow("Smile Selfie - Pressione 'c' (sorriso) ou 'q'", frame)
            cv2.waitKey(500)
        else:
            print("❌ Sem sorriso. Sorria e pressione 'c' novamente.")
            cv2.putText(frame, "SEM SORRISO - Foto NAO tirada", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.imshow("Smile Selfie - Pressione 'c' (sorriso) ou 'q'", frame)
            cv2.waitKey(500)

cap.release()
cv2.destroyAllWindows()