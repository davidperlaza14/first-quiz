package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements  VendingMachine {
  private  int balance; // Saldo actual del usuario
  private Map<String, Drink> drinks; // Mapa que almacena las bebidas disponibles

  public  VendingMachineImpl() {
    this.balance = 0; // Inicializa el saldo en 0
    this.drinks = new HashMap<>(); // Inicializa el mapa de bebidas

    // Agrega las bebidas disponibles y sus precios al mapa
    drinks.put("ScottCola", new DrinkImpl("ScottCola", true, 75));
    drinks.put("KarenTea", new DrinkImpl("KarenTea", false, 100));
  }

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    this.balance += 25; // Agrega 25 centavos al saldo cuando se inserta un cuarto
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    Drink selectedDrink = drinks.get(name); // Obtiene la bebida seleccionada por nombre

    if (selectedDrink == null){
      throw  new UnknownDrinkException(); // Si la vevida no existe, lanza una excepcion
    }

    if (balance < selectedDrink.getPrice()) {
      throw new NotEnoughMoneyException(); // Si el saldo no es suficiente, lanza una excepcion
    }

    balance -= selectedDrink.getPrice(); // Resta el precio de la bebida al saldo

    return selectedDrink; // Devuelve la bebida seleccionada
  }
}
