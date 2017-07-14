documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ] # Словарь с документами

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      } #Словарь с полками
      
# Запрос ввода
def input_comand():
  comand = input()
  return comand
        
# Номер_документа/имя (список док., номер док. )       
def people(documents, number_document):
  for people_name in documents:
    if number_document == people_name.get("number"):
      print(people_name.get('name'))
      return
  print('Документ не найден')
  return

# Список всех документов
def list_documents(documents):
  for i, docs in enumerate(documents):
    print('{0} {1} {2} {3}'.format(i + 1, docs.get('type'), docs.get('number'), docs.get('name')))
  return

# Номер полки по номеру документа (список полок, номер док. )
def number_folder(directories, number_document):
  for shelf, values in directories.items():
    for number_doc in values:
      if number_document == number_doc:
        print(shelf)
        return
  print('Документ не найден')
  return

# Список слов введеных пользователем через пробел(строка с данными через пробел)
def make_list_with_data(data):
  text = list()
  
  simbol = 1
  
  while simbol < len(data):
    if data[simbol - 1] != ' ':
      # начало среза
      start = simbol - 1
      # определяем индекс следующего пробела и делаем его концом среза
      while data[simbol] != ' ':
        simbol += 1
        # проверяем выход за пределя строки
        if simbol + 1 > len(data):
          break
      # добавляем срез между двумя пробелами в множество
      text.append(data[start : simbol])
      simbol += 1
    else:
      simbol += 1
  
  if len(text) == 4:
    text[2] = text[2] + ' ' + text[3]
    del text[3]
    
  return text

# Создание нового документа
def add_document():
  print('Введите через пробел данные документа (тип, номер, имя_владельца)', end = ' ')
  data_doc = make_list_with_data(input_comand())
  keys = ['type', 'number', 'name']
  doc = dict()
  for position in range(3):
    doc[keys[position]] = data_doc[position]
  return doc
  
# Добавление документа в список документов
def add_document_on_list(documents):
  documents.append(add_document())
  
# Проверки существования полки(список полок, номер целевой полки)
def old_shelf(directories, shelf):
  for key in directories.keys():
    if key == shelf:
      return shelf
      
# Добавление новой полки
def add_shelf_new(directories):
  print('Введите номер полки для добавления', end = ' ')
  shelf = input_comand()
  for key in directories.keys():
    if key == shelf:
      print('Полка {} уже существует'.format(shelf))
      return
  directories[shelf] = []
  
# Добавление номера документа на полку(добавленный док, директория, полка)
def add_number_doc_on_shelf(document, directories, shelf):
  for key, value in directories.items():
    if key == shelf:
      value.append(document['number'])
  return document
  
# Удаление документа по номеру(список док., номер документа)
def delete_document(documents, number_document):
  for doc in range(len(documents)):
    if documents[doc].get('number') == number_document:
      del documents[doc]
      return 1
      
# Удаление номера документа из списка полок(список полок, номер док.)
def delete_number_shelf(directories, number_document):
  for key, value in directories.items():
    for number in range(len(value)):
      if value[number] == number_document:
        del value[number]
        
# Добавление номера документа в список полок(директория, номер полки, номер документа)
def add_number_shelf(directories, number_shelf, number_document):
  for key, value in directories.items():
    if key == number_shelf:
     value.append(number_document)
        
# Перемещение документа(директория, номер полки, номер документа)
def document_move(directories, number_shelf, number_document):
  delete_number_shelf(directories, number_document)
  add_number_shelf(directories, number_shelf, number_document)

# Функция бесконечного ввода  
def main():
  while True:
    print('Введите команду:', end=' ')
    result_comand = input_comand()
    if result_comand == 'p' or result_comand == 'people':
      print('Введите номер документа:', end=' ')
      number_document = input_comand()
      people(documents, number_document)
    elif result_comand == 'l' or result_comand == 'list':
      list_documents(documents)
    elif result_comand == 's' or result_comand == 'shelf':
      print('Введите номер документа:', end=' ')
      number_document = input_comand()
      number_folder(directories,number_document)
    elif result_comand == 'a' or result_comand == 'add':
      print('Введите номер полки', end = ' ')
      shelf = input_comand()
      if old_shelf(directories, shelf) == None:
        print('Такой полки не сцществует')
        continue
      else:
        add_document_on_list(documents)
        add_number_doc_on_shelf(documents[len(documents) - 1], directories, shelf)
        print('Список документов:\n',documents)
        print('Список полок:\n',directories)
    elif result_comand == 'd' or result_comand == 'delete':
      print('Введите номер документа для удаления:', end = ' ')
      number_document_delete = input_comand()
      if delete_document(documents, number_document_delete) == None:
        print("Такого документа не существует.")
        continue
      else:
        print('Список документов после удаления:')
        list_documents(documents)
        delete_number_shelf(directories, number_document_delete)
        print('Список документов на полках:\n',directories)
    elif result_comand == 'm' or result_comand == 'move':
      print('Введите номер документа для перемещения:', end = ' ')
      number_document_move = input_comand()
      print('Введите номер целевой полки', end = ' ')
      number_shelf_move = input_comand()
      document_move(directories, number_shelf_move, number_document_move)
      print('Список документов на полках:\n',directories)
    elif result_comand == 'as' or result_comand == 'add shelf':
      add_shelf_new(directories)
      print (directories)

main()