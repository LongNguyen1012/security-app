from dockercheck import DockerControl
if __name__ == '__main__':
    run_cont = DockerControl()
    
    # To run a container named "nodejstest"
    run_cont.run_container('nodejstest',command='')
    
    # To stop a continer
    run_cont.stop_container("elegant_satoshi")