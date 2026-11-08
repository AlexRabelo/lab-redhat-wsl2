#!/usr/bin/env python3
"""Processa as imagens do lab RHEL + WSL2 conforme o padrão de design.

Aplica: redimensionamento 16:9 (1200x675), fundo #08090c, borda raio 8px
cor #1e293b, sombra suave. Não consegue borrar PII automaticamente — revisar manualmente.
"""
from PIL import Image, ImageDraw
import os
import sys

IMG_DIR = "assets/imgs/lab-rhel-wsl2"
TARGET_W, TARGET_H = 1200, 675  # 16:9
BORDER_COLOR = "#1e293b"
BORDER_RADIUS = 16
SHADOW_OFFSET = 14
SHADOW_ALPHA = 90


def add_shadow(canvas, img_w, img_h, offset_x, offset_y):
    """Desenha uma sombra arredondada atrás da imagem no canvas."""
    shadow = Image.new("RGBA", (img_w, img_h), (0, 0, 0, SHADOW_ALPHA))
    mask = Image.new("L", (img_w, img_h), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle([0, 0, img_w, img_h], radius=BORDER_RADIUS, fill=255)
    canvas.paste(shadow, (offset_x + SHADOW_OFFSET, offset_y + SHADOW_OFFSET), mask)


def add_border(canvas, img_w, img_h, offset_x, offset_y):
    """Desenha a borda arredondada por cima da imagem."""
    border = Image.new("RGBA", (img_w, img_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(border)
    draw.rounded_rectangle(
        [0, 0, img_w - 1, img_h - 1],
        radius=BORDER_RADIUS,
        outline=BORDER_COLOR,
        width=6,
    )
    canvas.alpha_composite(border, dest=(offset_x, offset_y))


def process_image(path):
    img = Image.open(path).convert("RGBA")

    # Redimensionar mantendo proporção, cabendo dentro de 1200x675
    img.thumbnail((TARGET_W - SHADOW_OFFSET * 2, TARGET_H - SHADOW_OFFSET * 2), Image.LANCZOS)

    # Canvas com espaço para a sombra
    canvas_w = img.width + SHADOW_OFFSET * 2
    canvas_h = img.height + SHADOW_OFFSET * 2
    # Se menor que alvo, preencher até o alvo
    canvas_w = max(canvas_w, TARGET_W)
    canvas_h = max(canvas_h, TARGET_H)

    canvas = Image.new("RGBA", (canvas_w, canvas_h), "#08090c" + "ff")

    # Centralizar imagem no canvas
    offset_x = (canvas_w - img.width) // 2
    offset_y = (canvas_h - img.height) // 2

    # Desenhar sombra atrás
    add_shadow(canvas, img.width, img.height, offset_x, offset_y)

    # Colar imagem
    canvas.paste(img, (offset_x, offset_y), img)

    # Desenhar borda por cima
    add_border(canvas, img.width, img.height, offset_x, offset_y)

    # Converter para RGB e salvar
    result = canvas.convert("RGB")
    result.save(path, "PNG", optimize=True)
    return result.size


def main():
    if not os.path.isdir(IMG_DIR):
        print(f"Diretório não encontrado: {IMG_DIR}")
        sys.exit(1)

    files = sorted(f for f in os.listdir(IMG_DIR) if f.lower().endswith(".png"))
    if not files:
        print("Nenhuma imagem PNG encontrada.")
        sys.exit(1)

    print(f"Processando {len(files)} imagens em {IMG_DIR}/")
    print("-" * 60)
    for fname in files:
        path = os.path.join(IMG_DIR, fname)
        try:
            new_size = process_image(path)
            print(f"OK  {fname:35s} -> {new_size[0]}x{new_size[1]}")
        except Exception as e:
            print(f"ERRO {fname}: {e}")

    print("-" * 60)
    print("Concluído. Revise manualmente o borrado de PII em cada imagem.")
    print("Dados a borrar: nome de usuário Windows, e-mail Red Hat, IPs, chaves.")


if __name__ == "__main__":
    main()
