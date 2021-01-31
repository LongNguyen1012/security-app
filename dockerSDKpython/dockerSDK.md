# requirements: 
    docker library -> pip install docker

**Docker provides an API for interacting with the docker Deamon**

1. Run a conitainer
```python
    import docker 
    client = docker.from_env()
    print(client.containers.run("alpine", ["echo", "hello", "world"])
```

2. Stop all running containers
```python
    import docker 
    client = docker.from_env()
    for container in client.containers.list():
        container.stop()
```

3. List all images
```python
    import docker 
    client = docker.from_env()
    for image in client.images.list():
        print(images.id)
```

4. Pull an image
```python
    import docker
    client = docker.from_env()
    image = client.images.pull('alpine')
```

5. We can do something like:
    - List and manage containers
    - Print the logs of the specific container
    - Commit a container

## Documentation
    https://docker-py.readthedocs.io/en/stable/containers.html