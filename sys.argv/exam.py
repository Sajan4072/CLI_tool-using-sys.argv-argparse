from PySide2 import QtWidgets

info={
    "task1":{"status":"In progress","assigned to":"emp1"},
    "task2":{"status":"New","assigned to":"emp2"}

}

def display_info(id,query_key):
    #start a Qt app
    app=QtWidgets.QApplication()
    
    task=info.get(id,None)
    if task:
        if query_key:
            infor=info[id][query_key]
            data="{} {} is {}".format(id,query_key,infor)
        else:
            data="{} {}".format(id,info[id])
    else:
        data="{} doesnot exist".format(id)

    QtWidgets.QMessageBox.information(None,'Task Info Tool',data)


display_info('task1','status')  



    
