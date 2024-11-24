from services.agenda_services import exit_program
from menu import menu_services, services_involving_contacts
from data import contact_list

while True:
  print(f"\n=== Agenda em Python ===")
  print(f"\nO que deseja fazer?")

  services_list = menu_services.copy()
  if contact_list:
    services_list.extend(services_involving_contacts)
  services_list.append({"label": "Sair", "service": exit_program})

  for i, service in enumerate(services_list):
    if i == 0:
      print()
    print(f"{i + 1}. {service['label']}")

  choice = input(f"\nSelecione uma opção para continuar: ")

  try:
    choice = int(choice) - 1
    if 0 <= choice < len(services_list):
      services_list[choice]["service"]()
    else:
      print("\nOpção inválida. Tente novamente.")
  except ValueError:
    print("\nEntrada inválida. Por favor, insira um número.")