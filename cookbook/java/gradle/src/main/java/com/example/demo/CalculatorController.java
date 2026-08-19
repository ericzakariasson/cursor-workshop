package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;

@RestController
@CrossOrigin(origins = "*")
public class CalculatorController {
  @GetMapping("/add")
  public String add(@RequestParam int a, @RequestParam int b) {
    return "The sum of " + a + " and " + b + " is " + (a + b);
  }
  
  @GetMapping("/subtract")
  public String subtract(@RequestParam int a, @RequestParam int b) {
    return "The difference of " + a + " and " + b + " is " + (a - b);
  }

  @GetMapping("/multiply")
  public String multiply(@RequestParam int a, @RequestParam int b) {
    return "The product of " + a + " and " + b + " is " + (a * b);
  }

  @GetMapping("/divide")
  public String divide(@RequestParam int a, @RequestParam int b) {
    return "The quotient of " + a + " and " + b + " is " + (a / b);
  }

  @GetMapping("/square")
  public String square(@RequestParam int a) {
    return "The square of " + a + " is " + (a * a);
  }
} 