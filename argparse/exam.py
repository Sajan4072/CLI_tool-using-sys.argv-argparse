from PySide2 import QtWidgets
import sys
import argparse

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


if __name__=='__main__':

    parser=argparse.ArgumentParser(prog='exam',
                                usage='''
                                Pass the exam task data in json format 
                                and this will return the value from query key.      
                                ''',
                                description='''
                                This tool will display exam information
                                ----------------------------------------
                                    
                                ''',
                                epilog="Copyright@Sajan",
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                add_help=True 

                                )
            
    parser.add_argument("task",type=str,help="Enter id for example:Task1",metavar="ID")
    parser.add_argument("--key","-k",type=str,
                        help="Optional:Enter query key to  search information for eg:status",default='status',
                        required=False
                        )
    arg=parser.parse_args()
    display_info(arg.task,arg.key)                  

                                    
                                
   