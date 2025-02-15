-- Create: basedados/categorias.sql

CREATE TABLE CATEGORIES (
  CODIGO SERIAL PRIMARY KEY,
  NAME VARCHAR(50) NOT NULL,
  TYPE VARCHAR(20) CHECK (type IN ('receita', 'gasto essencial', 'gasto não essencial'))
)

-- Insert: basedados/categorias.sql

INSERT INTO categories (name, type) VALUES
('Salário', 'receita'),
('Renda Extra', 'receita'),
('Mercado', 'gasto essencial'),
('Moradia', 'gasto essencial'),
('Desenvolvimento', 'gasto essencial'),
('Investimento', 'gasto essencial'),
('Transporte', 'gasto essencial'),
('Lazer', 'gasto não essencial'),
('Comida fora', 'gasto não essencial'),
('Assinatura', 'gasto não essencial'),
('Saúde', 'gasto essencial'),
('Educação', 'gasto essencial'),
('Compras', 'gasto não essencial'),
('Viagem', 'gasto não essencial');


