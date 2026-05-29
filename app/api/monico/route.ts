import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const { message } = await req.json();
  
  // Simple Jarvis response - in full version would connect to model
  const response = `Monico here, bro. You said: ${message}. I'm ready to create accounts and businesses.`;
  
  return NextResponse.json({ response });
}