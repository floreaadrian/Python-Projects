from domain.driver import drivers

class driverCon:

    def __init__(self,repo):
        '''

        :param repo: is the repo class in which we have access to data
        '''
        self._repo= repo

    def findId(self,id):
        '''
        We call the findId function in repo
        :return: True if id is found and False if is not found
        '''
        return self._repo.findId(id)