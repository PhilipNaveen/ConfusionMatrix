using System;

public class ConfusionMatrix{
    //instance variables
    double TP;
    double TN;
    double FP;
    double FN;
    
    //constructor: ConfusionMatrix
    public ConfusionMatrix(bool[] predicted_series, bool[] actual_series){
        for (int j = 0; j < predicted_series.Length; j++){
            if (predicted_series[j] == true && actual_series[j] == true){
                TP++;
            }
            else if (predicted_series[j] == false && actual_series[j] == false){
                TN++;
            }
            else if (predicted_series[j] == true && actual_series[j] == false){
                FP++;
            }
            else if (predicted_series[j] == false && actual_series[j] == true){
                FN++;
            }
            else{
                //do nothing
            }
        }
    }
    
    //getter methods: TP, TN, FP, FN
    public int TruePositives(){
        return (int)TP;
    }
    
    public int TrueNegatives(){
        return (int)TN;
    }
    
    public int FalsePositives(){
        return (int)FP;
    }
    
    public int FalseNegatives(){
        return (int)FN;
    }
    
   //getter methods: accuracy, specificity, sensitivity, etc.
   public double Accuracy(){
       return 100 * ((TP + TN)/(TP + TN + FP + FN));
   }
   
   public double Specificity(){
       return 100 * ((TN)/(TN + FP));
   }
   
   public double Sensitivity(){
       return 100 * ((TP)/(TP + FN));
   }
   
   public double NegativePredictiveValue(){
       return 100 * ((TN)/(TN + FN));
   }
   
   //regualized summary of ConfusionMatrix
   public void PrintMetrics(){
       Console.WriteLine("-----Metrics of ConfusionMatrix-----");
       Console.WriteLine("True Positives: " + TP);
       Console.WriteLine("True Negatives: " + TN);
       Console.WriteLine("False Positives: " + FP);
       Console.WriteLine("False Negatives: " + FN);
       Console.WriteLine();
       Console.WriteLine("Specificity: " + Specificity());
       Console.WriteLine("Sensitivity: " + Sensitivity());
       Console.WriteLine("Negative Predictive Value: " + NegativePredictiveValue());
       Console.WriteLine("Accuracy: " + Accuracy());
   }
   
   //returns the amount of each prediction
   public string ToString(){
       return TP + " " + TN + " " + FP + " " + FN;
   }
}
