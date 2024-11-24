def exit_program():
  print(f"\nPrograma Agenda em Python finalizado.")
  exit()

def add_contact(contact_list=None):
  if contact_list is None:  
    contact_list = []

  contact_name = ''
  while not contact_name: 
    name = input(f"\nNome: ")
    if not name.strip():
        print('Nome é obrigatório')
    else:
        contact_name = name.strip()
    
  contact_email = ''
  while not contact_email:  
    email = input("E-mail: ")
    if not email.strip():
        print('E-mail é obrigatório')
    else:
        contact_email = email.strip()

  phone = input("Telefone (opcional): ").strip()
  
  new_contact = {"name": contact_name, "email": contact_email, "phone": phone, "favorite": False}

  contact_list.append(new_contact)

  print(f"\n{new_contact['name']} adicionado a lista de contatos com sucesso!")

  return 

def visualize_contact_list(contact_list, only_favorites=False):
  if only_favorites:
    print("\n--- Lista de Contatos Favoritos ---")
  else:
    print("\n--- Lista de Contatos ---")

  filtered_contacts = contact_list if not only_favorites else [contato for contato in contact_list if contato["favorite"]]

  if not filtered_contacts:
    print(f"\nNenhum contato encontrado.")

  for i, contato in enumerate(filtered_contacts, 1):
    favorite = "★" if contato["favorite"] else " "

    print(f"\n{i}. [{favorite}] Nome: {contato['name']},")
    print(f"       E-mail: {contato['email']},")
    if contato["phone"]:
      print(f"       Telefone: {contato['phone']},")

def edit_contact(contact_list):
  visualize_contact_list(contact_list)

  try:
    contact_index = int(input(f"\nSelecione o índice do contato que deseja editar: ")) - 1
    if contact_index < 0 or contact_index >= len(contact_list):
      print(f"\nÍndice inválido. Tente novamente.")
      return

    selected_contact = contact_list[contact_index]

    print(f"\nEditando o contato: {selected_contact['name']}")
    new_name = input("Novo nome (ou pressione ENTER para manter o atual): ").strip()
    new_email = input("Novo e-mail (ou pressione ENTER para manter o atual): ").strip()
    new_phone = input("Novo telefone (ou pressione ENTER para manter o atual): ").strip()

    if new_name:
      selected_contact['name'] = new_name
    if new_email:
      selected_contact['email'] = new_email
    if new_phone:
      selected_contact['phone'] = new_phone

    print(f"\nContato atualizado com sucesso!")
  except ValueError:
      print("\nEntrada inválida. Insira um índice válido.")

def favorite_and_unfavorite_contact(contact_list):
  visualize_contact_list(contact_list)

  try:
    contact_index = int(input(f"\nSelecione o índice do contato que deseja marcar / desmarcar como favorito: ")) - 1
    if contact_index < 0 or contact_index >= len(contact_list):
      print(f"\nÍndice inválido. Tente novamente.")
      return

    selected_contact = contact_list[contact_index]

    if selected_contact:
      selected_contact['favorite'] = not selected_contact['favorite']

    if selected_contact['favorite']:
      print(f"\nContato favoritado com sucesso!")
    else:
      print(f"\nContato desfavoritado com sucesso!")
  except ValueError:
    print("\nEntrada inválida. Insira um índice válido.")

def delete_contact(contact_list=None):
  if contact_list is None:  
    contact_list = []

  visualize_contact_list(contact_list)

  try:
    contact_index = int(input(f"\nSelecione o índice do contato que deseja apagar: ")) - 1
    if contact_index < 0 or contact_index >= len(contact_list):
      print(f"\nÍndice inválido. Tente novamente.")
      return

    selected_contact = contact_list[contact_index]

    if selected_contact:
      contact_list.remove(selected_contact)
    
    print(f"\nContato apagado com sucesso!")
  except ValueError:
    print("\nEntrada inválida. Insira um índice válido.")