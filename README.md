# FFMSP-SA-Metaheuristic

Reposotorio dedicado al desarrollo de la segunda iteración del problema semestral para Sistemas Adaptativos.

Integrantes: 
        - Emilio Meza 
        - Ana Vargas

En esta iteración se explorará el problema FFMSP, con el objetivo de crear un GRASP con la condición de máximo tiempo de ejecución. Este repositoria consiste de un archivo principal llamado "grasp.py".

    -grasp.py : Este programa se encarga de ejecutar nuestro grasp el cual guardara la mejor respuesta y se encontrara en bucle mientras el tiempo no se acabe 
    
Este archivo .py posee un argumento -h el cual indica el correcto uso de este, el cual sería:
    -python3 grasp.py -i [Filename] -t [MaxTimeInSeconds]
Siendo Filename obviamente el nombre de los archivos a testear y MaxTimeInSeconds el numero maximo de segundos los cuales el programa se ejecutará.
