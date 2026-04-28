import cv2

for i in range(5):
    print(f"Testando índice {i}...", end=" ")
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret and frame is not None:
            print(f"✅ Funcionou! Índice {i} está mostrando vídeo.")
            cv2.imshow(f"Câmera {i}", frame)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
        else:
            print(f"⚠️ Abriu mas não capturou frame.")
        cap.release()
    else:
        print(f"❌ Falhou.")