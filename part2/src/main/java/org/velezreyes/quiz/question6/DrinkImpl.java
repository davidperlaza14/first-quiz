package org.velezreyes.quiz.question6;

class DrinkImpl implements Drink {
    private String name; // Nombre da la bebida
    private boolean fizzy; // Indica si la bebida es efervescente
    private int price; // Precio de la bebida encentavos

    public DrinkImpl(String name, boolean fizzy, int price) {
        this.name = name;
        this.fizzy = fizzy;
        this.price = price;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return fizzy;
    }

    public  int getPrice() {
        return price;
    }
}
