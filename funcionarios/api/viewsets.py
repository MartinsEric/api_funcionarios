from rest_framework.viewsets import ModelViewSet
from funcionarios.models import Funcionario
from .serializers import FuncionarioSerializer
import logging

logger = logging.getLogger(__name__)


class FuncionarioViewSet(ModelViewSet):

    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def create(self, request, *args, **kwargs):

        """
        Cria um funcionário no banco de dados.
        """

        logger.info('POST')

        return super(FuncionarioViewSet, self).create( request, *args, **kwargs)

    def list(self, request, *args, **kwargs):

        """
        Retorna a lista de todos os funcionários.
        """

        logger.info('GET')

        return super(FuncionarioViewSet, self).list( request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):

        """
        Retorna um único funcionário identificado pelo ID.
        """

        logger.info('GET')

        return super(FuncionarioViewSet, self).retrieve( request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        """
        Atualiza as informações de um funcinário identificado pelo ID.
        """

        logger.info('PUT')

        return super(FuncionarioViewSet, self).update( request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):

        """
        Atualiza parcialmente as informações de um funcionário identificado pelo ID.
        """

        logger.info('PATCH')

        return super(FuncionarioViewSet, self).partial_update( request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):

        """
        Deleta um funcionário identificado pelo seu ID.
        """

        logger.info('DELETE')

        return super(FuncionarioViewSet, self).destroy( request, *args, **kwargs)

