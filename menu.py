from services.agenda_services import add_contact, visualize_contact_list, edit_contact, favorite_and_unfavorite_contact, delete_contact  
from data import contact_list

menu_services = [
  {"label": "Adicionar contato", "service": lambda: add_contact(contact_list)},
]

services_involving_contacts = [
  {"label": "Visualizar a lista de contatos", "service": lambda: visualize_contact_list(contact_list)},
  {"label": "Editar contato", "service": lambda: edit_contact(contact_list)},
  {"label": "Marcar/desmarcar contato como favorito", "service": lambda: favorite_and_unfavorite_contact(contact_list)},
  {"label": "Ver lista de contatos favoritos", "service": lambda: visualize_contact_list(contact_list, True)},
  {"label": "Apagar contato", "service": lambda: delete_contact(contact_list)},
]