# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# A simple python script that allows you to add and replace the columns within a project in MySQL Workbench
# Written in MySQL Workbench 5.2.47
# Dev Igor Campus <igor.campus@gmail.com>

import grt
#import mforms

# Imposto il datatype
datatypes = grt.root.wb.rdbmsMgmt.rdbms[0].simpleDatatypes

# Prelevo il primo schema del modello
schema = grt.root.wb.doc.physicalModels[0].catalog.schemata[0]

# Colonna create_date
column_create = grt.classes.db_mysql_Column()
column_create.name = "create_date"
column_create.setParseType("DATETIME", datatypes)
#column_create.defaultValue = "CURRENT_TIMESTAMP"


# Colonna last_update
column_update = grt.classes.db_mysql_Column()
column_update.name = "last_update"
column_update.setParseType("TIMESTAMP", datatypes)
column_update.defaultValue = "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"


# Effettuo un ciclo per tutte le tabelle del db
for table in schema.tables:
    


    #print table.name 
    for column in table.columns:
        if column.name == "create_date" or column.name == "last_update":
            table.removeColumn(column);
    
    
    

    # Aggiungo la colonna alla tabella
    table.addColumn(column_create);
    table.addColumn(column_update);






