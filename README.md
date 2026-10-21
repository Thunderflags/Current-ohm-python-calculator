# Electrical Circuit Calculator

# 1. About the Project
This is a beginner-level Python project I made to relate to my LED circuit experiment using the Falstad Circuit Simulator. It calculates current or resistance in a simple electrical circuit, with or without an LED.

# 2. Objective
The objective is to understand Ohm's law and compare theoretical calculations with the values obtained from my Falstad circuit simulation.

# 3. Features
- Calculates current in amperes (A) and milliamperes (mA).
- Calculates resistance in ohms (Ω).
- Supports circuits with or without an LED.
- Checks for invalid inputs and displays error messages.

# 4. Formulas Used

**Without an LED:**

- Current: `I = V / R`
- Resistance: `R = V / I`

**With an LED:**

- Current: `I = (Vs - Vf) / R`
- Resistance: `R = (Vs - Vf) / I`

Here, `Vs` is the supply voltage, `Vf` is the LED forward voltage, `I` is current, and `R` is resistance.

# 5. Meaning of Variables

| Variable | Meaning |
|---|---|
| `S_V` | Supply voltage in volts |
| `L_V` | LED forward voltage in volts |
| `R` | Resistance in ohms |
| `I` | Current in amperes |
| `led_choice` | Checks whether an LED is included |
| `find` | Stores whether the user wants current or resistance |
| `ValueError` | Handles inputs that cannot be converted into numbers |

# 6. How to Use
1. Run the Python program.
2. Enter the supply voltage.
3. Enter `y` to include an LED or `n` to exclude it.
4. Choose `current` or `resistance` and enter the requested value.
5. Read the calculated result displayed on the screen.

# 7. Example Calculation

For a 5 V supply, a 2 V LED forward voltage, and a 220 Ω resistor:

`I = (5 - 2) / 220`

`I = 0.01364 A = 13.64 mA`

This is the estimated current for the LED circuit.

# 8. Connection to My Falstad Experiment
I made this calculator to support my LED circuit experiment and understand how resistance affects current. I can compare the theoretical result with the simulated current.

**Falstad Circuit:** https://www.falstad.com/s.py?s=LhRh49

# 9. Limitations
The program assumes a fixed LED forward voltage and uses basic circuit formulas. Actual LED behaviour may differ because its forward voltage can vary with current and the LED model.

# 10. Technologies Used
- Python 3
- Falstad Circuit Simulator

# 11. Conclusion
This project helped me apply Ohm's law using Python and understand the relationship between voltage, current, and resistance. It also connects programming concepts with my basic electrical engineering experiment.
