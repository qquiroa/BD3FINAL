<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Pago extends Model
{
    protected $table = 'pago';

    protected $fillable = [
        'correlativo',
        'cui',
        'id_estado',
        'id_tipopago',
        'fecha',
        'fechamod',
        'no_boleto',
        'id_cajero'
        
    ];
    protected $hidden = ['created_at','updated_at'];

}
