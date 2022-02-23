from ai_benchmark import AIBenchmark
results = AIBenchmark().run()
##save the result to .txt
with open('result.txt', 'a') as f:
    f.write("\nDevice Inference Score: " + str(results.inference_score))
    f.write("Device Training Score: " + str(results.training_score))
    f.write("Device AI Score: " + str(results.ai_score) + "\n")