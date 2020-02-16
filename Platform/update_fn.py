import pandas

def data_update(di):
      dl = pandas.DataFrame()

      for i in range(len(di)):
            dz = pandas.DataFrame(data=di[i], index=[i])
            dl = dl.append(dz)
            
      dl.to_excel('Canteen.xlsx', index = False)
      return "\n Database successfully updated!"
