# LLM Council (Native Antigravity Version)

![llmcouncil](header.jpg)

Este repositorio es una implementación nativa del **Consejo de Deliberación** para Google Antigravity. En lugar de ser una aplicación web externa, funciona como una **Skill** integrada que permite al agente resolver problemas complejos mediante un proceso de inteligencia colectiva en 3 etapas.

## 🚀 Antigravity Skill Integration
Este proyecto es **100% Antigravity Compatible**. No requiere APIs externas ni configuración de OpenRouter; utiliza tus modelos locales de Antigravity.

### Instalación
1.  **Clona este repo** en tu carpeta de proyectos.
2.  **Registra la Skill**: Copia el archivo `SKILL.md` a tu directorio global de skills (típicamente `~/.agents/skills/llm-council/SKILL.md`).
3.  **¡Listo!**: Antigravity detectará automáticamente las reglas en `.agents/rules/` y los flujos en `.agents/workflows/`.

---

## 🧠 ¿Cómo funciona? (El Protocolo)

El consejo opera en 3 fases críticas para garantizar la máxima precisión:

1.  **Etapa 1: Colección (Divergencia)**
    *   Se generan 3 perspectivas técnicas independientes.
    *   Agentes: **Gemini Flash 3**, **Gemini Pro 3.1 Low** y **Sonnet Thinking 4.6**.

2.  **Etapa 2: Ranking (Crítica Anonimizada)**
    *   Los agentes revisan las respuestas de los demás sin conocer sus identidades para evitar sesgos.
    *   Se genera un ranking de precisión y profundidad técnica.

3.  **Etapa 3: Síntesis (Convergencia)**
    *   El **Chairman** (**Gemini Pro 3.1 High**) analiza los rankings y las respuestas para producir una solución final consolidada.

---

## 🛠️ Uso y Comandos

### Desde el Chat (Recomendado)
Simplemente pídele a Antigravity que realice una deliberación:
- `/deliberate [Tu consulta compleja]`
- "Realiza una deliberación sobre este problema de arquitectura..."

### Desde la Terminal (Modo Tool)
Para integraciones o scripts, puedes llamar al adaptador de la skill:
```bash
python -m backend.skill_adapter "Tu consulta"
```

---

## 🏗️ Estructura del Proyecto
- `.agents/`: Reglas y Workflows para la integración nativa.
- `backend/skill_adapter.py`: Puente de ejecución para la terminal.
- `SKILL.md`: Definición global de la capacidad del agente.
- `graphify-out/`: (Opcional) Mapa visual de la arquitectura generado por Graphify.

---

## 📜 Créditos
Basado en el concepto original de `karpathy/llm-council`, adaptado y forkeado para ser una Skill nativa de alto rendimiento en entornos Agénticos.
