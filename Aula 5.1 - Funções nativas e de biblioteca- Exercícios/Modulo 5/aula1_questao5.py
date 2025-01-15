import emoji

def main():
    # Lista de emojis disponíveis
    emojis_disponiveis = {
        "❤️": ":red_heart:",
        "👍": ":thumbs_up:",
        "🤔": ":thinking_face:",
        "🥳": ":partying_face:"
    }

    # Exibe os emojis disponíveis para o usuário
    print("Emojis disponíveis:")
    for simbolo, codigo in emojis_disponiveis.items():
        print(f"{simbolo} - {codigo}")

    # Solicita uma frase ao usuário
    frase_codificada = input("\nDigite uma frase com os códigos de emoji acima e ela será emojizada:\n")

    # Converte os códigos de emoji na representação visual
    frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

    # Exibe a frase emojizada
    print("\nFrase emojizada:")
    print(frase_emojizada)

# Executa o programa
if __name__ == "__main__":
    main()
