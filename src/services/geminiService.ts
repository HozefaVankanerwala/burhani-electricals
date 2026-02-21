import { GoogleGenAI } from "@google/genai";

// Initialize the Gemini client
const ai = new GoogleGenAI({ apiKey: import.meta.env.VITE_GEMINI_API_KEY || '' });

export const generateAssistantResponse = async (userMessage: string): Promise<string> => {
  try {
    const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: userMessage,
      config: {
        systemInstruction: `You are the friendly and knowledgeable AI assistant for "Burhani Electrical's". 
        The business is owned by Mr. Husain M Vankanerwala.
        Services include: Repairing and rewinding of all types of fans (Ceiling, Wall, Table, Cabin, Pedestal, Stand, Tower, Exhaust, Mini Exhaust, Talvar, Farata, Lift fans), Mixer/Blender repairing, Iron repairing, and Geyser repairing.
        
        Your Goal:
        1. Answer basic questions about appliance maintenance (e.g., why a fan is noisy, why a mixer isn't starting).
        2. Provide simple troubleshooting tips.
        3. ALWAYS conclude by suggesting the user contact Mr. Husain M Vankanerwala at +91 8780514062 or visit the shop for a professional repair quote.
        4. Keep answers concise, professional, and polite. 
        5. If asked about prices, say "Prices vary based on the specific issue. Please call Mr. Husain for an accurate quote."
        `,
        temperature: 0.7,
      }
    });

    return response.text || "I'm having trouble thinking right now. Please call us directly!";
  } catch (error) {
    console.error("Gemini API Error:", error);
    return "I'm currently experiencing technical difficulties. Please contact Husain directly at +91 8780514062.";
  }
};