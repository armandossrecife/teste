package com.example.demo;

public class Usuario {
    private String usuario;
    private String nome;
    private String email;
    private String senha;

    // Adicione getters e setters para os campos acima
    public String getNome(){
        return this.nome;
    }
    public String getEmail(){
        return this.email;
    }
    public String getSenha(){
        return this.senha;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setEmail(String email){
        this.email = email;
    }
    public void setSenha(String senha){
        this.senha = senha;
    }
}