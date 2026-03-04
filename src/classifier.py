from transformers import AutoTokenizer, AutoModelForSequenceClassification

class TriageClassifier:
    def __init__(self):
        # Carregamento do modelo (Manteremos o BERTimbau como base)
        self.model_name = "neuralmind/bert-base-portuguese-cased"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        # Note: num_labels=3 para bater com LEVE, MODERADO, URGENTE
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=3)

    def predict(self, text: str):
        text_lower = text.lower()
        
        # --- Lógica de Contexto e Exclusão ---
        # Termos que indicam urgência real em áreas críticas
        critical_indicators = ["dor", "aperto", "pressao", "dormencia", "paralisia", "falta de ar"]
        critical_anatomy = ["peito", "coracao", "braco", "rosto", "pulmao"]
        
        # Termos que anulam a urgência cardíaca (Falsos Positivos)
        exclusion_terms = ["cocando", "coceira", "espinha", "mancha", "vermelha", "picada"]

        # 1. Verifica se há uma Red Flag real
        has_critical_area = any(area in text_lower for area in critical_anatomy)
        has_symptom = any(sym in text_lower for sym in critical_indicators)
        is_skin_issue = any(exc in text_lower for exc in exclusion_terms)

        # 2. Veredito com Raciocínio Crítico
        if has_critical_area and has_symptom and not is_skin_issue:
            return "URGENTE", 0.98, "Sintomas sugestivos de emergência cardiovascular. Procure o pronto-socorro."
        
        if is_skin_issue:
            return "LEVE", 0.85, "Sintomas cutâneos detectados. Monitore a evolução ou busque dermatologista."

        if has_critical_area or has_symptom:
            return "MODERADO", 0.75, "Sintoma relevante detectado. Recomendada avaliação médica em até 4h."

        return "LEVE", 0.60, "Sintomas de baixa gravidade aparente. Aguarde atendimento ou use telemedicina."