<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class Pago extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('pagos', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->int("correlativo");
            $table->int("cui");
            $table->int("id_estado");
            $table->int("id_tipopago");
            $table->date("fecha");
            $table->date("fechamod");
            $table->int("no_boleto");
            $table->int("id_cajero");


        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('pagos');
    }
}
