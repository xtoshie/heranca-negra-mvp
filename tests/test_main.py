import sqlite3
import pytest
from src.main import inicializar_banco, cadastrar_conteudo, listar_conteudos, consultar_conteudo

@pytest.fixture
def banco():
    conexao = sqlite3.connect(":memory:")
    inicializar_banco(conexao)
    yield conexao
    conexao.close()

def test_acervo_inicialmente_vazio(banco):
    assert listar_conteudos(banco) == []

def test_cadastro_e_listagem_de_audio(banco):
    cadastrar_conteudo(banco, "Toque de Angola", "audio", "assets/audio/angola.mp3")
    assert listar_conteudos(banco, "audio")[0][1] == "Toque de Angola"

def test_filtrar_textos(banco):
    cadastrar_conteudo(banco, "História da capoeira", "texto", "assets/textos/historia.txt")
    cadastrar_conteudo(banco, "Toque de Angola", "audio", "assets/audio/angola.mp3")
    assert len(listar_conteudos(banco, "texto")) == 1

def test_consultar_por_id(banco):
    identificador = cadastrar_conteudo(banco, "História", "texto", "historia.txt")
    assert consultar_conteudo(banco, identificador)[1] == "História"

@pytest.mark.parametrize("titulo,categoria,caminho", [("", "audio", "x.mp3"), ("Teste", "video", "x.mp4"), ("Teste", "texto", "")])
def test_rejeitar_dados_invalidos(banco, titulo, categoria, caminho):
    with pytest.raises(ValueError):
        cadastrar_conteudo(banco, titulo, categoria, caminho)

def test_categoria_invalida(banco):
    with pytest.raises(ValueError):
        listar_conteudos(banco, "video")

def test_consulta_inexistente(banco):
    assert consultar_conteudo(banco, 999) is None
