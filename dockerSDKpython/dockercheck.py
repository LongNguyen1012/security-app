import docker

class DockerControl:
    client = docker.from_env()
    
    # Parameter: 
        # image_name(str) : name of image
        # command(str): command when start the container
    def run_container(self, image_name, *args):
        container = self.client.containers.run(image_name, *args)
        return container

    # Parameter: containerInfor(str) : name or Id of the container
    # Return a container object
    def get_container(self,containerInfor):
        try:
            return self.client.containers.get(containerInfor)
        except:
            raise docker.error.NotFound
    
    # Parameter: 
        # name(str): name or ID of the container which you want to stop
    def stop_container(self, name=""):
        for container in self.client.containers.list():
            if container.name == name or container.id in name:
                container.stop()
        
    # Parameter: 
        # name(str): name of the image you want to pull
    def pull_image(self, name=""):
        self.client.images.pull(name)

    # Parameter: 
        # name(str): name of the image you want to pull
    def list_container(self):
        output = []
        container_list = self.client.containers.list()
        for c in container_list:
            output.append(c.name)
        return output
