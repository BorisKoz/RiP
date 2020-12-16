from abc import ABC, abstractmethod


# порождающий паттерн проектирования
# абстрактная фабрика
# предметная область:

class Motherboard(ABC):
    @abstractmethod
    def install (self):
        pass

class Processor(ABC):
    @abstractmethod
    def install (self, motherboard_type):
        pass

class GPU(ABC):
    @abstractmethod
    def install (self):
        pass

class PC_Factory(ABC):
    @abstractmethod
    def install_motherboard(self):
        pass

    @abstractmethod
    def install_processor(self):
        pass

    @abstractmethod
    def install_gpu(self):
        pass

    @abstractmethod
    def price(self):
        pass

class Intel_Motherboard(Motherboard):
    def install (self):
        return "установлена плата с чипсетом INTEL"
    m_type = "I"
    price = 110

class AMD_Motherboard(Motherboard):
    def install(self):
        return "установлена плата с чипсетом AMD"
    m_type = "A"
    price =100

class Intel_Processor(Processor):
    def install(self, motherboard_type):
        if motherboard_type.m_type == "I":
            return "установлен процессор INTEL"
        else:
            return "неверный тип платы"
    price = 200

class AMD_Processor(Processor):
    def install(self, motherboard_type):
        if motherboard_type.m_type == "A":
            return "установлен процессор AMD"
        else:
            return "неверный тип платы"
    price =180


class Nvidia_GPU(GPU):
    def install (self):
        return "установлена видеокарта Nvidia"
    price =220

class AMD_GPU (GPU):
    def install(self):
        return "установлена видеокарта AMD"
    price =200

class Intel_Nvidia(PC_Factory):
    def install_motherboard(self):
        return Intel_Motherboard()
    def install_processor(self):
        return Intel_Processor()
    def install_gpu(self):
        return Nvidia_GPU()
    def price (self):
        return Intel_Motherboard.price+Intel_Processor.price+Nvidia_GPU.price

class Intel_AMD(PC_Factory):
    def install_motherboard(self):
        return Intel_Motherboard()
    def install_processor(self):
        return Intel_Processor()
    def install_gpu(self):
        return AMD_GPU()
    def price (self):
        return Intel_Motherboard.price+Intel_Processor.price+AMD_GPU.price


class AMD_AMD(PC_Factory):
    def install_motherboard(self):
        return AMD_Motherboard()
    def install_processor(self):
        return AMD_Processor()
    def install_gpu(self):
        return AMD_GPU()
    def price (self):
        return AMD_Motherboard.price+AMD_Processor.price+AMD_GPU.price


def client_code(factory):
    mb = factory.install_motherboard()
    proc = factory.install_processor()
    gpu = factory.install_gpu()

    print (mb.install())
    print (proc.install(mb))
    print (gpu.install())
    print (factory.price())


if __name__ == '__main__':

    client_code(AMD_AMD())
    print('\n')
    client_code(Intel_Nvidia())
    print('\n')
    client_code(Intel_AMD())
