const express = require('express');
const bcrypt = require('bcrypt');
const app = express();
const port = 3000;

// Configuração do Express para lidar com dados do formulário
app.use(express.urlencoded({ extended: false }));

// Rota para exibir o formulário de cadastro
app.get('/', (req, res) => {
  res.send(`
    <h1>Formulário de Cadastro de Usuário</h1>
    <form method="POST" action="/cadastro">
      <label for="usuario">Usuário:</label>
      <input type="text" id="usuario" name="usuario" required><br><br>
      <label for="nome">Nome Completo:</label>
      <input type="text" id="nome" name="nome" required><br><br>
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required><br><br>
      <label for="senha">Senha:</label>
      <input type="password" id="senha" name="senha" required><br><br>
      <input type="submit" value="Cadastrar">
    </form>
  `);
});

// Rota para processar o formulário de cadastro
app.post('/cadastro', async (req, res) => {
  const { usuario, nome, email, senha } = req.body;

  // Simulação de salvamento em um banco de dados
  const hashedPassword = await bcrypt.hash(senha, 10);

  res.send(`
    <h1>Usuário Cadastrado</h1>
    <p>Usuário: ${usuario}</p>
    <p>Nome Completo: ${nome}</p>
    <p>Email: ${email}</p>
  `);
});

// Inicia o servidor na porta especificada
app.listen(port, () => {
  console.log(`Servidor iniciado em http://localhost:${port}`);
});
