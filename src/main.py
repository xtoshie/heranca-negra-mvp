"""Núcleo mínimo do acervo cultural Herança Negra Musicalidade."""
import sqlite3

def inicializar_banco(conexao):
    conexao.execute("""CREATE TABLE IF NOT EXISTS acervo_cultural (
        id_conteudo INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        categoria TEXT NOT NULL CHECK(categoria IN ('audio', 'texto')),
        caminho_arquivo TEXT NOT NULL,
        descricao TEXT DEFAULT ''
    )""")
    conexao.commit()

def cadastrar_conteudo(conexao, titulo, categoria, caminho_arquivo, descricao=""):
    if not titulo.strip() or categoria not in ("audio", "texto") or not caminho_arquivo.strip():
        raise ValueError("Conteúdo inválido")
    cursor = conexao.execute(
        "INSERT INTO acervo_cultural (titulo, categoria, caminho_arquivo, descricao) VALUES (?, ?, ?, ?)",
        (titulo.strip(), categoria, caminho_arquivo.strip(), descricao),
    )
    conexao.commit()
    return cursor.lastrowid

def listar_conteudos(conexao, categoria=None):
    if categoria is not None and categoria not in ("audio", "texto"):
        raise ValueError("Categoria inválida")
    if categoria is None:
        cursor = conexao.execute("SELECT id_conteudo, titulo, categoria, caminho_arquivo, descricao FROM acervo_cultural ORDER BY titulo")
    else:
        cursor = conexao.execute("SELECT id_conteudo, titulo, categoria, caminho_arquivo, descricao FROM acervo_cultural WHERE categoria = ? ORDER BY titulo", (categoria,))
    return cursor.fetchall()

def consultar_conteudo(conexao, id_conteudo):
    return conexao.execute("SELECT id_conteudo, titulo, categoria, caminho_arquivo, descricao FROM acervo_cultural WHERE id_conteudo = ?", (id_conteudo,)).fetchone()
