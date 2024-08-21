# @app.route('/getupload', methods=['POST','GET'])
# def getupload():
#     try :
#         if request.method == 'POST':
#             print(request)
#             name=request.form['name']
#             contents_folder=os.path.join(app.root_path, 'contents')
#             print('contents_folder',contents_folder)
#             file_path = os.path.join(contents_folder, name)
#             print('file_path',file_path)
#             tdata =pd.read_csv(file_path).to_json(orient='records')
#             return jsonify({"msg":"success","tdata":tdata})
#     except Exception as e :
#         print(e)
#         return jsonify({"msg":"fail","data":e})

# @app.route('/getdashboard', methods=['POST','GET'])
# def getdashboard():
#     try :
#         if request.method == 'GET':
#             tdata =pd.read_excel("Dashboard.xlsx") #.to_json(orient='records')
#             dash = tdata.to_dict('list')
#             result = {dash['Updation_date'][i].strftime('%Y-%m-%d'): dash['Dashboard'][i].split(", ") for i in range(len(dash['Dashboard']))}
#             print(result)
#             return jsonify({"msg":"success","tdata":result})
#     except Exception as e :
#         print(e)
#         return jsonify({"msg":"fail","data":e})  