import pandas as pd


def SearchEDV(InputedEDV):
    try:
        df = pd.read_excel('./registros.xlsx')

        data = df[df['EDV'] == InputedEDV]
        data = data.values[0]
        obj = {
            'EDV': data[0],
            'Nome': data[1],
            'Email': data[2],
            'Telefone': data[3]
        }
        return obj, 200
    except:
        return 'EDV não encontrado', 404


def registerUser(cursor, data):
    # try:
    cursor.execute(
        'insert into users values({},"{}","{}","{}")'.format(data['EDV'], data['Name'], data['Email'], data['Phone']))
    a = cursor.connection.commit()
    return data, 201
# except:
#     return 'Houve um erro', 500
