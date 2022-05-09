## SISTEMA PARA PODOLOGOS
### O usuario pode ser admin e usuario paciente/cliente
### O usuario pode ser: do tipo paciente ou usuario do tipo admin

#### usuario admin (autenticado) - usuarios/paciente(pode ser definido com cliente):
    - pode cadastar usuario
    - pode deletar usuario
    - pode atualizar usuario
    - pode listar usuarios
    - pode lista um usuario


 #### usuario admin (autenticado) - paciente(pode ser definido com cliente):
    - pode cadastrar um paciente
    - pode atualizar um paciente
    - pode deletar um paciente(softdelete atualizar para deletado as patologias referente a esse paciente)
    - pode ver todos os pacientes
    - pode ver um paciente em especifico

#### usuario admin (autenticado) - atendimento:
    - pode marcar um atendimento
    - pode cancelar um atendimento

    - pode registar as patologias do paciente
    - pode atualizar as patologias do paciente 
    - atendimento não pode ser apagado

#### usuario admin (autenticado) - tarefas:
    - pode criar tarefas
    - pode concluir tarefas

#### usuarios paciente - sistema (possivelmente um applicativo mobile):
    - pode ver a agenda do podologo
    - pode marcar um atendimento
    - não pode desmarcar um atendimento (para desmarcar é nescessario ligar na clinica)
