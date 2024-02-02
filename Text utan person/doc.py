def read_lines():
    all_names = []
    with open("konversation.txt") as file:
        for line in file:
            name = line.split(':')[0]
            if name not in all_names:
                all_names.append(name)
    
    return all_names


def filter_conversation(input_file, output_file, person_to_exclude):
    with open(input_file, 'r', encoding='utf-8') as file:
        conversation_lines = file.readlines()

    filtered_conversation = [line for line in conversation_lines if person_to_exclude not in line]

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(filtered_conversation)


if __name__ == "__main__":
    input_file_path = "konversation.txt"
    output_file_path = "filtrerad.txt"

    all_names = read_lines()

    person_to_exclude = input(f"Vem av {all_names} vill du ta bort?")

    filter_conversation(input_file_path, output_file_path, person_to_exclude)

    print(f"Filtered conversation saved to {output_file_path}")