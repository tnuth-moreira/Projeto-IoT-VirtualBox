# Projeto IoT com VirtualBox Linux

Este projeto foi desenvolvido para a disciplina de **Fundamentos de Internet das Coisas (IoT)**, usando uma **máquina virtual Linux (VirtualBox)** para conectar sensores e enviar dados para o **ThingSpeak**.

## Tecnologias Utilizadas

- VirtualBox com Linux
- Python e MicroPython
- Sensor DHT11
- Protocolo HTTP para comunicação com ThingSpeak
- Módulo de Relé

## Descrição do Projeto

O projeto utiliza um sensor **DHT11** para monitorar temperatura e umidade, e um módulo de relé que é ativado quando os limites de temperatura ou umidade são excedidos. Os dados são enviados para o **ThingSpeak**, uma plataforma de IoT para visualização dos dados coletados.

### Como Configurar

1. Clone o repositório:

   ```bash
   git clone https://github.com/tnuth-moreira/Projeto-IoT-VirtualBox.git
   ```

2. Configure o Wi-Fi e o sensor DHT11 no código.

3 .Execute o código em um dispositivo compatível com MicroPython.
