import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function sum(...numbers: number[]): number {
  // Add all numbers in the array together starting from 0
  return numbers.reduce(
    (accumulator, currentNumber) => accumulator + currentNumber,
    0
  );
}

export function multiply(...numbers: number[]): number {
  return numbers.reduce(
    (accumulator, currentNumber) => accumulator * currentNumber,
    1
  );
}
