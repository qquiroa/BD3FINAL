<?php

namespace App\Http\Controllers;

use App\Pago;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class PagoController extends Controller
{
    
    public function show($id)
    {
        try {
            $info = Pago::where('cui','=',$id)->firstOrFail();
            return response()->json([
                'success' => true,
                'message' =>'CUI buscado',
                'data'    => $info
            ], 200);
        } catch (\Throwable $th) {
            return response()->json(['message' => "El CUI numero {$id} no Ha realizado ningún pago"], 404);
        }                
    } //fin de show


    
}
