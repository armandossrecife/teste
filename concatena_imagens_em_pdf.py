from PIL import Image
import os
import glob

# Configurações
pasta_imagens = "reuniao"  # Altere para o caminho da sua pasta
arquivo_saida = "reunia_modelo_gestao.pdf"

# Encontrar todas as imagens PNG
imagens = sorted(glob.glob(os.path.join(pasta_imagens, "*.png")))

if not imagens:
    print("Nenhuma imagem PNG encontrada!")
else:
    # Converter imagens para RGB
    imagens_rgb = []
    for img_path in imagens:
        img = Image.open(img_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        imagens_rgb.append(img)
    
    # Salvar como PDF
    imagens_rgb[0].save(
        arquivo_saida,
        save_all=True,
        append_images=imagens_rgb[1:]
    )
    
    print(f"PDF criado com {len(imagens)} páginas: {arquivo_saida}")
