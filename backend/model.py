import os, time, torch, transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline



class TinyLlamaLLM():
    def __init__(self):
        self.model_name_or_path = 'TheBloke/TinyLlama-1.1B-Chat-v1.0-GPTQ'
        self.model_file = 'tinyllama-1.1b-chat-v0.3.Q5_K_S.gguf'
        print('Initializing TinyLlamaLLM Model')
        self.check_gpu_is_available()
        self.model, self.tokenizer = self.load_llm()

    def check_gpu_is_available(self):
        print(torch.cuda.is_available())
        if torch.cuda.is_available():
            print("Cuda is Availabe")
        else:
            print("Cuda Can't be found")

    def load_llm(self):
        model = AutoModelForCausalLM.from_pretrained(self.model_name_or_path,
                                                    device_map="auto",
                                                    )
        tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path,
                                            use_fast=True)
        return model, tokenizer

    def create_prompt(self, tokenizer, usr_prompt):
        text = """
        Instruct: Write a detailed analogy between mathematics and a lighthouse.\n
        Output:
        """

        if type(usr_prompt) != str:
            print('prompt is not a String')
            return ''
        messages = [
            {
                "role": "system",
                "content": "You are a friendly chatbot who always responds in the style of a pirate",
            },
            {"role": "user", "content": usr_prompt},
        ]

        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        print(prompt)
        return prompt

    def generate_output(self, usr_prompt):
        prompt = self.create_prompt(self.tokenizer, usr_prompt)
        input_ids = self.tokenizer(prompt, return_tensors='pt').input_ids.cuda()

        start = time.time()
        print("\n\n*** Generate:")
        output = self.model.generate(inputs=input_ids,
                                temperature=0.7,
                                do_sample=True,
                                top_p=0.95,
                                top_k=40,
                                max_new_tokens=512)
        response = self.tokenizer.decode(output[0])
        print(self.tokenizer.decode(output[0]))
        end = time.time()
        run_time = end - start
        print(f'Time elapsed: {run_time}')
        return response.split('\n<|assistant|>\n')[1].replace('</s>', '')


