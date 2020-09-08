%    This is the machine generated representation of a SimBiology
%    session.
% 
%    To run the session save this MATLAB file and type the name of the MATLAB file 
%    at the MATLAB command prompt. The MATLAB file must be on your MATLAB PATH.
%    For additional information on setting your MATLAB PATH, type 'help addpath'
%    at the MATLAB command prompt.
  
%    Creation time: 31-Aug-2020 01:52 PM

% Create SimBiology Model.
m1 = sbiomodel('heat_shock_re');

% Add component(s) to SimBiology Model.
c1 = addcompartment(m1, 'unnamed');

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\Documents\MATLAB\heat_shock_re.sbproj', 'm1');
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm1');

% Add component(s) to SimBiology Model.
s1 = addspecies(c1, 'species_1');

% Rename component.
rename(s1, 'NatP');

% Add component(s) to SimBiology Model.
s2 = addspecies(c1, 'species_1');

% Rename component.
rename(s2, 'MisP');

% Add component(s) to SimBiology Model.
s3 = addspecies(c1, 'species_1');

% Rename component.
rename(s3, 'AggP');

% Add component(s) to SimBiology Model.
r1 = addreaction(m1, 'null -> null');

% Configure properties.
set(r1, 'Name', 'reaction_1');
set(r1, 'Reaction', 'NatP -> null');
set(r1, 'Reversible', false);
set(r1, 'Reaction', 'NatP -> null');
set(r1, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k1 = m1.Reactions(1).KineticLaw(1);

% Add component(s) to SimBiology Model.
p1 = addparameter(k1, 'kf', 1.0);

% Configure properties.
set(r1, 'Reaction', 'NatP -> MisP');
set(r1, 'Reversible', false);
set(r1, 'Reaction', 'NatP -> MisP');

% Add component(s) to SimBiology Model.
r2 = addreaction(m1, 'null -> null');

% Configure properties.
set(r2, 'Name', 'reaction_2');
set(r2, 'Reaction', 'MisP -> null');
set(r2, 'Reversible', false);
set(r2, 'Reaction', 'MisP -> null');
set(r2, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k2 = m1.Reactions(2).KineticLaw(1);

% Add component(s) to SimBiology Model.
p2 = addparameter(k2, 'kf', 1.0);

% Configure properties.
set(r2, 'Reaction', 'MisP -> AggP');
set(r2, 'Reversible', false);
set(r2, 'Reaction', 'MisP -> AggP');

% Add component(s) to SimBiology Model.
s4 = addspecies(c1, 'species_1');
p3 = addparameter(m1, 'parameter_1', 1.0);

% Delete object(s).
delete(m1.Parameters(1));

% Rename component.
rename(s4, 'HSP90&MisP');

% Add component(s) to SimBiology Model.
r3 = addreaction(m1, 'null -> null');

% Configure properties.
set(r3, 'Name', 'reaction_3');
set(r3, 'Reaction', 'MisP -> null');
set(r3, 'Reversible', false);
set(r3, 'Reaction', 'MisP -> null');
set(r3, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k3 = m1.Reactions(3).KineticLaw(1);

% Add component(s) to SimBiology Model.
p4 = addparameter(k3, 'kf', 1.0);

% Configure properties.
set(r3, 'Reaction', 'MisP -> [HSP90&MisP]');
set(r3, 'Reversible', false);
set(r3, 'Reaction', 'MisP -> [HSP90&MisP]');

% Rename component.
rename(c1, 'Cell');

% Add component(s) to SimBiology Model.
s5 = addspecies(c1, 'species_1');

% Rename component.
rename(s5, 'HSP90 ');

% Configure properties.
set(r3, 'Reaction', 'MisP + HSP90 -> [HSP90&MisP]');
set(r3, 'Reversible', false);
set(r3, 'Reaction', 'MisP + HSP90 -> [HSP90&MisP]');

% Rename component.
rename(r1, 'Misfolding');

% Configure properties.
set(k1, 'KineticLawName', 'MassAction');
set(k1, 'ParameterVariableNames', {'kf'});

% Rename component.
rename(r3, 'Binding');

% Configure properties.
set(r3, 'Reaction', 'MisP + HSP90 <-> [HSP90&MisP]');
set(r3, 'Reversible', true);

% Add component(s) to SimBiology Model.
p5 = addparameter(k3, 'Kr', 1.0);

% Configure properties.
set(k3, 'ParameterVariableNames', {'kf','Kr'});
set(r3, 'Reaction', 'MisP + HSP90 -> [HSP90&MisP]');
set(r3, 'Reversible', false);
set(r3, 'Reaction', 'MisP + HSP90 <-> [HSP90&MisP]');
set(r3, 'Reversible', true);
set(p1, 'Value', 2.0E-5);
set(p1, 'ValueUnits', 'mole^-1*s^-1');
set(p1, 'ValueUnits', '1/(mole*second)');

% Rename component.
rename(r2, 'Aggregation');

% Configure properties.
set(p1, 'Name', 'k1');
set(k1, 'ParameterVariableNames', {'k1'});

% Rename component.
rename(p1, 'k2');

% Configure properties.
set(p2, 'Name', 'k7');
set(k2, 'ParameterVariableNames', {'k7'});
set(r3, 'Reaction', 'MisP + HSP90 + [HSP90&MisP] <-> [HSP90&MisP]');
set(r3, 'Reversible', true);
set(r3, 'Reaction', 'MisP + HSP90 + [HSP90&MisP] <-> [HSP90&MisP]');
set(r3, 'Reaction', 'MisP + HSP90 + [HSP90&MisP] <-> [HSP90&MisP] + HSP90');
set(r3, 'Reversible', true);
set(r3, 'Reaction', 'MisP + HSP90 + [HSP90&MisP] <-> [HSP90&MisP] + HSP90');
set(r3, 'Reaction', 'MisP + HSP90 + [HSP90&MisP] <-> [HSP90&MisP] + HSP90 + MisP');
set(r3, 'Reversible', true);
set(r3, 'Reaction', 'MisP + HSP90 + [HSP90&MisP] <-> [HSP90&MisP] + HSP90 + MisP');
set(r3, 'Reversible', true);
set(r3, 'Reaction', 'MisP + HSP90 <-> [HSP90&MisP]');

% Add component(s) to SimBiology Model.
p6 = addparameter(k3, 'kr', 1.0);

% Configure properties.
set(k3, 'ParameterVariableNames', {'kf','kr'});
set(p4, 'Value', 50.0);
set(p4, 'Name', 'k3');
set(k3, 'ParameterVariableNames', {'k3','kr'});
set(p4, 'ValueUnits', '1/(mole*second)');
set(p6, 'Name', 'k4');
set(k3, 'ParameterVariableNames', {'k3','k4'});
set(p6, 'Value', 1.0E-5);
set(p6, 'ValueUnits', '1/(mole*second)');

% Add component(s) to SimBiology Model.
p7 = addparameter(k3, 'Kr1', 1.0);

% Configure properties.
set(p6, 'ValueUnits', 'mixed');
set(p5, 'ValueUnits', 'mixed');
set(p7, 'ValueUnits', 'mixed');

% Delete object(s).
delete(m1.Reactions(3).KineticLaw(1).Parameters(2));
delete(m1.Reactions(3).KineticLaw(1).Parameters(3));

% Configure properties.
set(p2, 'Value', 1.0E-7);
set(p2, 'ValueUnits', '1/(mole*second)');

% Add component(s) to SimBiology Model.
r4 = addreaction(m1, 'null -> null');

% Configure properties.
set(r4, 'Name', 'reaction_1');
set(r4, 'Reaction', '[HSP90&MisP] -> null');
set(r4, 'Reversible', false);
set(r4, 'Reaction', '[HSP90&MisP] -> null');
set(r4, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k4 = m1.Reactions(4).KineticLaw(1);

% Add component(s) to SimBiology Model.
p8 = addparameter(k4, 'kf', 1.0);

% Configure properties.
set(r4, 'Reaction', '[HSP90&MisP] -> HSP90');
set(r4, 'Reversible', false);
set(r4, 'Reaction', '[HSP90&MisP] -> HSP90');
set(r4, 'Reaction', '[HSP90&MisP] -> HSP90 + NatP');
set(r4, 'Reversible', false);
set(r4, 'Reaction', '[HSP90&MisP] -> HSP90 + NatP');

% Rename component.
rename(r4, 'Refolding');

% Configure properties.
set(p8, 'ValueUnits', '1/(mole*second)');
set(p8, 'Name', 'k5');
set(k4, 'ParameterVariableNames', {'k5'});
set(p8, 'Value', 4.0E-6);

% Add component(s) to SimBiology Model.
r5 = addreaction(m1, 'null -> null');

% Configure properties.
set(r5, 'Name', 'reaction_1');
set(r5, 'Reaction', 'MisP -> null');
set(r5, 'Reversible', false);
set(r5, 'Reaction', 'MisP -> null');
set(r5, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k5 = m1.Reactions(5).KineticLaw(1);

% Add component(s) to SimBiology Model.
p9 = addparameter(k5, 'kf', 1.0);

% Rename component.
rename(r5, 'Degredation');
rename(r5, 'Degradation');

% Configure properties.
set(p9, 'Name', 'k6');
set(k5, 'ParameterVariableNames', {'k6'});
set(p9, 'Value', 6.0E-7);
set(p9, 'ValueUnits', '1/(mole*second)');

% Add component(s) to SimBiology Model.
r6 = addreaction(m1, 'null -> null');

% Configure properties.
set(r6, 'Name', 'reaction_1');
set(r6, 'Reaction', 'null -> NatP');
set(r6, 'Reversible', false);
set(r6, 'Reaction', 'null -> NatP');
set(r6, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k6 = m1.Reactions(6).KineticLaw(1);

% Add component(s) to SimBiology Model.
p10 = addparameter(k6, 'kf', 1.0);

% Rename component.
rename(r6, 'Protein Synthesis');

% Configure properties.
set(p10, 'Name', 'k1');
set(k6, 'ParameterVariableNames', {'k1'});
set(p10, 'Value', 10.0);
set(p10, 'ValueUnits', 'mole/second');
set(s1, 'InitialAmountUnits', 'mole');
set(s1, 'InitialAmount', 6000000.0);
set(s1, 'InitialAmountUnits', 'molecule');
set(s5, 'InitialAmount', 300000.0);
set(s5, 'InitialAmountUnits', 'molecule');

% Assign variable name to object.
cs1 = getconfigset(m1, 'default');

% Configure properties.
set(cs1, 'StopTime', 1.0);
set(cs1, 'StopTime', 1.0);
set(cs1, 'TimeUnits', 'minute');
set(cs1, 'TimeUnits', 'minute');
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'TimeUnits', 'second');
set(cs1, 'TimeUnits', 'second');
set(cs1.CompileOptions, 'UnitConversion', true);
set(cs1.CompileOptions, 'UnitConversion', true);

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm1');

% Configure properties.
set(s1, 'InitialAmountUnits', 'mole');
set(s5, 'InitialAmountUnits', 'mole');
set(s1, 'InitialAmount', 6.0);
set(s5, 'InitialAmount', 4.0);
set(s5, 'InitialAmount', 3.0);
set(p1, 'ValueUnits', '1/second');
set(p2, 'ValueUnits', '1/second');

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(p4, 'ValueUnits', '1/(molarity*second)');
set(p6, 'ValueUnits', '1/second');
set(s5, 'InitialAmountUnits', 'molarity');
set(s1, 'InitialAmountUnits', 'molarity');
set(c1, 'CapacityUnits', 'molecule');
set(c1, 'CapacityUnits', 'molarity');
set(c1, 'CapacityUnits', '');
set(c1, 'CapacityUnits', 'number');
set(c1, 'CapacityUnits', '');
set(c1, 'CapacityUnits', 'mole');
set(c1, 'CapacityUnits', 'volume');
set(c1, 'CapacityUnits', 'length');
set(c1, 'CapacityUnits', 'mme3');
set(c1, 'CapacityUnits', 'mm3');
set(c1, 'CapacityUnits', 'mm^(3)');
set(c1, 'CapacityUnits', 'milimetre sqare');
set(c1, 'CapacityUnits', 'milimetresqare');
set(c1, 'CapacityUnits', 'cm');
set(c1, 'CapacityUnits', 'k');
set(c1, 'CapacityUnits', 'volume');
set(c1, 'CapacityUnits', 'mole');
set(c1, 'CapacityUnits', 'centimetre');
set(c1, 'CapacityUnits', 'cubic millimetre');
set(c1, 'CapacityUnits', 'microlitre');
set(p8, 'ValueUnits', '1/second');
set(p9, 'ValueUnits', 'second');
set(p9, 'ValueUnits', '1/second');

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(s2, 'InitialAmountUnits', 'molarity');
set(s3, 'InitialAmountUnits', 'molarity');
set(s4, 'InitialAmountUnits', 'molarity');

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(s1, 'InitialAmountUnits', 'molecules');
set(s1, 'InitialAmountUnits', 'molecule');
set(s1, 'InitialAmount', 6000000.0);
set(s5, 'InitialAmount', 300000.0);
set(s5, 'InitialAmountUnits', 'molecule');
set(s5, 'InitialAmountUnits', 'molarity');
set(s5, 'InitialAmount', 4.9816172E-16);
set(s1, 'InitialAmount', 9.9632344E-15);
set(s1, 'InitialAmountUnits', 'molarity');
set(p10, 'ValueUnits', '1/second');
set(p10, 'ValueUnits', 'molarity/second');
set(p10, 'Value', 1.0);
set(p10, 'Value', 1.0E-20);
set(p10, 'Value', 10.0);

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm1');

% Configure properties.
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);
set(p8, 'Value', 40.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);
set(p8, 'Value', 4.0E-6);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);
set(p8, 'Value', 4.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);

% Rename component.
rename(c1, 'Heat_shock');

% Add component(s) to SimBiology Model.
c2 = addcompartment(m1, 'compartment_1');

% Configure properties.
set(r1, 'Reaction', 'Heat_shock.NatP -> Heat_shock.MisP');
set(r4, 'Reaction', 'Heat_shock.[HSP90&MisP] -> Heat_shock.HSP90 + Heat_shock.NatP');
set(r2, 'Reaction', 'Heat_shock.MisP -> Heat_shock.AggP');
set(r5, 'Reaction', 'Heat_shock.MisP -> null');
set(r3, 'Reaction', 'Heat_shock.MisP + Heat_shock.HSP90 <-> Heat_shock.[HSP90&MisP]');
set(r6, 'Reaction', 'null -> Heat_shock.NatP');
set(p8, 'Value', 4.0E-6);

% Rename component.
rename(c2, 'Autoregulation of ');
rename(c2, 'Autoregulation of HSP90');

% Configure properties.
set(c2, 'ConstantCapacity', false);
set(c2, 'ConstantCapacity', true);

% Add component(s) to SimBiology Model.
s6 = addspecies(c2, 'species_1');

% Rename component.
rename(s6, 'HSF1');

% Add component(s) to SimBiology Model.
s7 = addspecies(c2, 'species_1');

% Rename component.
rename(s7, 'HSP90');

% Add component(s) to SimBiology Model.
s8 = addspecies(c2, 'species_1');

% Rename component.
rename(s8, 'HSF1&HSP90');

% Add component(s) to SimBiology Model.
r7 = addreaction(m1, 'null -> null');

% Configure properties.
set(r7, 'Name', 'reaction_1');
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 -> null');
set(r7, 'Reversible', false);
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 -> null');
set(r7, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k7 = m1.Reactions(7).KineticLaw(1);

% Add component(s) to SimBiology Model.
p11 = addparameter(k7, 'kf', 1.0);

% Configure properties.
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 + [Autoregulation of HSP90].HSP90 -> null');
set(r7, 'Reversible', false);
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 + [Autoregulation of HSP90].HSP90 -> null');
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 -> null');
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 + [Autoregulation of HSP90].[HSF1&HSP90] -> null');
set(r7, 'Reversible', false);
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 + [Autoregulation of HSP90].[HSF1&HSP90] -> null');
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 + [Autoregulation of HSP90].[HSF1&HSP90] <-> null');
set(r7, 'Reversible', true);
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 + [Autoregulation of HSP90].[HSF1&HSP90] + [Autoregulation of HSP90].HSP90 <-> null');
set(r7, 'Reversible', true);
set(r7, 'Reaction', '[Autoregulation of HSP90].HSF1 + [Autoregulation of HSP90].[HSF1&HSP90] + [Autoregulation of HSP90].HSP90 <-> null');

% Rename component.
rename(c2, 'Autoregulation');

% Configure properties.
set(r7, 'Reversible', true);
set(r7, 'Reaction', 'Autoregulation.HSF1 + Autoregulation.HSP90 <-> Autoregulation.[HSF1&HSP90]');
set(p11, 'Name', 'k8');
set(k7, 'ParameterVariableNames', {'k8',''});

% Add component(s) to SimBiology Model.
p12 = addparameter(k7, 'k9', 1.0);

% Configure properties.
set(k7, 'ParameterVariableNames', {'k8','k9'});
set(p11, 'ValueUnits', '1/second');
set(p11, 'ValueUnits', '1/(molarity*second)');
set(p12, 'ValueUnits', '1/second');

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm1');

% Configure properties.
set(p11, 'Value', 500.0);

% Add component(s) to SimBiology Model.
s9 = addspecies(c2, 'species_1');
s10 = addspecies(c2, 'species_2');
s11 = addspecies(c2, 'species_3');

% Rename component.
rename(s9, 'DiH');
rename(s10, 'TriH');
rename(s11, 'HSE');

% Add component(s) to SimBiology Model.
s12 = addspecies(c2, 'HSE1');

% Rename component.
rename(s12, 'TriH&HSE');

% Add component(s) to SimBiology Model.
r8 = addreaction(m1, 'null -> null');

% Configure properties.
set(r8, 'Name', 'reaction_2');

% Add component(s) to SimBiology Model.
r9 = addreaction(m1, 'null -> null');

% Configure properties.
set(r9, 'Name', 'reaction_3');
set(r9, 'Name', 'reaction_3');
set(r9, 'ReactionRate', '');

% Add component(s) to SimBiology Model.
r10 = addreaction(m1, 'null -> null');

% Configure properties.
set(r10, 'Name', 'reaction_4');
set(r10, 'Name', 'reaction_4');
set(r10, 'ReactionRate', '');

% Assign variable name to object.
r11 = m1.Reactions(11);

% Configure properties.
set(r11, 'Name', 'reaction_5');
set(r11, 'ReactionRate', '');
set(r8, 'Reaction', 'Autoregulation.HSF1 -> null');
set(r8, 'Reversible', false);
set(r8, 'Reaction', 'Autoregulation.HSF1 -> null');
set(r8, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k8 = m1.Reactions(8).KineticLaw(1);

% Add component(s) to SimBiology Model.
p13 = addparameter(k8, 'kf', 1.0);

% Configure properties.
set(r8, 'Reaction', 'Autoregulation.HSF1 -> Autoregulation.DiH');
set(r8, 'Reversible', false);
set(r8, 'Reaction', 'Autoregulation.HSF1 -> Autoregulation.DiH');

% Rename component.
rename(r7, 'HSF1_Binding');
rename(r8, 'Dimerisation');

% Configure properties.
set(r9, 'Reaction', 'Autoregulation.DiH -> null');
set(r9, 'Reversible', false);
set(r9, 'Reaction', 'Autoregulation.DiH -> null');
set(r9, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k9 = m1.Reactions(9).KineticLaw(1);

% Add component(s) to SimBiology Model.
p14 = addparameter(k9, 'kf', 1.0);

% Configure properties.
set(r9, 'Reaction', 'Autoregulation.DiH -> Autoregulation.TriH');
set(r9, 'Reversible', false);
set(r9, 'Reaction', 'Autoregulation.DiH -> Autoregulation.TriH');

% Rename component.
rename(r9, 'Trimerisation');

% Configure properties.
set(r8, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.DiH');
set(r8, 'Reversible', true);
set(p13, 'Name', 'k10');
set(k8, 'ParameterVariableNames', {'k10',''});

% Add component(s) to SimBiology Model.
p15 = addparameter(k8, 'k13', 1.0);

% Configure properties.
set(k8, 'ParameterVariableNames', {'k10','k13'});
set(r9, 'Reaction', 'Autoregulation.DiH <-> Autoregulation.TriH');
set(r9, 'Reversible', true);
set(p14, 'Name', 'k11');
set(k9, 'ParameterVariableNames', {'k11',''});

% Add component(s) to SimBiology Model.
p16 = addparameter(k9, 'k12', 1.0);

% Configure properties.
set(k9, 'ParameterVariableNames', {'k11','k12'});
set(r10, 'Reaction', 'Autoregulation.TriH -> null');
set(r10, 'Reversible', false);
set(r10, 'Reaction', 'Autoregulation.TriH -> null');
set(r10, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k10 = m1.Reactions(10).KineticLaw(1);

% Add component(s) to SimBiology Model.
p17 = addparameter(k10, 'kf', 1.0);

% Configure properties.
set(r10, 'Reaction', 'Autoregulation.TriH + Autoregulation.HSE -> null');
set(r10, 'Reversible', false);
set(r10, 'Reaction', 'Autoregulation.TriH + Autoregulation.HSE -> null');
set(r10, 'Reaction', 'Autoregulation.TriH + Autoregulation.HSE -> Autoregulation.[TriH&HSE]');
set(r10, 'Reversible', false);
set(r10, 'Reaction', 'Autoregulation.TriH + Autoregulation.HSE -> Autoregulation.[TriH&HSE]');
set(r10, 'Reaction', 'Autoregulation.TriH + Autoregulation.HSE <-> Autoregulation.[TriH&HSE]');
set(r10, 'Reversible', true);
set(p17, 'Name', 'k14');
set(k10, 'ParameterVariableNames', {'k14',''});

% Add component(s) to SimBiology Model.
p18 = addparameter(k10, 'k15', 1.0);

% Configure properties.
set(k10, 'ParameterVariableNames', {'k14','k15'});

% Rename component.
rename(r10, 'DNA_Binding');
rename(r11, 'synthesis');

% Configure properties.
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> null');
set(r11, 'Reversible', false);
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> null');
set(r11, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k11 = m1.Reactions(11).KineticLaw(1);

% Add component(s) to SimBiology Model.
p19 = addparameter(k11, 'kf', 1.0);

% Configure properties.
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.HSP90');
set(r11, 'Reversible', false);
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.HSP90');
set(r11, 'Reversible', false);
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.HSP90 + Autoregulation.[TriH&HSE]');

% Add component(s) to SimBiology Model.
r12 = addreaction(m1, 'Autoregulation.HSP90 -> Heat_shock.HSP90');

% Assign variable name to object.
k12 = m1.Reactions(12).KineticLaw(1);

% Add component(s) to SimBiology Model.
p20 = addparameter(k12, 'kf', 1.0);

% Rename component.
rename(r12, 'transfer');

% Configure properties.
set(p20, 'ValueUnits', '1/second');

% Verify the SimBiology Model.
verify(m1);

% Delete object(s).
delete(m1.Reactions(12));

% Configure properties.
set(r7, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r7, 'Reversible', true);
set(r7, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.[TriH&HSE]');
set(r11, 'Reversible', false);
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.[TriH&HSE]');

% Delete object(s).
delete(m1.Compartments(2).Species(2));

% Configure properties.
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.[TriH&HSE] + Heat_shock.HSP90');
set(r11, 'Reversible', false);
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.[TriH&HSE] + Heat_shock.HSP90');
set(r7, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90] + Heat_shock.HSP90');
set(r7, 'Reversible', true);
set(r7, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90] + Heat_shock.HSP90');
set(r7, 'Reversible', true);
set(r7, 'Reaction', 'Heat_shock.HSP90 + Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(p13, 'Value', 0.01);

% Add component(s) to SimBiology Model.
c3 = addcompartment(m1, '2Autoregulation');
s13 = addspecies(c3, 'HSF1');

% Configure properties.
set(r7, 'Reaction', 'Heat_shock.HSP90 + Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r1, 'Reaction', 'Heat_shock.NatP -> Heat_shock.MisP');
set(r4, 'Reaction', 'Heat_shock.[HSP90&MisP] -> Heat_shock.HSP90 + Heat_shock.NatP');
set(r2, 'Reaction', 'Heat_shock.MisP -> Heat_shock.AggP');
set(r8, 'Reversible', true);
set(r5, 'Reaction', 'Heat_shock.MisP -> null');
set(r3, 'Reaction', 'Heat_shock.MisP + Heat_shock.HSP90 <-> Heat_shock.[HSP90&MisP]');
set(r6, 'Reaction', 'null -> Heat_shock.NatP');
set(r9, 'Reaction', 'Autoregulation.DiH <-> Autoregulation.TriH');
set(r10, 'Reaction', 'Autoregulation.TriH + Autoregulation.HSE <-> Autoregulation.[TriH&HSE]');
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.[TriH&HSE] + Heat_shock.HSP90');
set(r8, 'Reaction', '[2Autoregulation].HSF1 <-> Autoregulation.DiH');
set(r8, 'Reversible', true);
set(r8, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.DiH');
set(r8, 'ReactionRate', 'k10*Autoregulation.HSF1^2 - k13*Autoregulation.DiH');
set(p13, 'ValueUnits', '1/(molarity*second)');
set(p15, 'Value', 0.5);
set(p15, 'ValueUnits', '1/second');
set(p14, 'Value', 100.0);
set(r9, 'Reaction', 'Autoregulation.DiH + Autoregulation.HSF1 <-> Autoregulation.TriH');
set(r9, 'Reversible', true);
set(r9, 'Reaction', 'Autoregulation.DiH + Autoregulation.HSF1 <-> Autoregulation.TriH');
set(p14, 'ValueUnits', '1/(molarity*second)');
set(p16, 'Value', 0.5);
set(p16, 'ValueUnits', '1/second');
set(p17, 'Value', 0.05);
set(p18, 'Value', 0.08);
set(p17, 'ValueUnits', 'mole');
set(p17, 'ValueUnits', '1/(molarity*second)');
set(p18, 'ValueUnits', '1/second');
set(s11, 'InitialAmount', 1.0);
set(s11, 'InitialAmountUnits', 'molecule');
set(s6, 'InitialAmount', 100.0);
set(s6, 'InitialAmountUnits', 'molecule');
set(s8, 'InitialAmount', 5900.0);
set(s8, 'InitialAmountUnits', 'molecule');
set(p19, 'Name', 'k16');
set(k11, 'ParameterVariableNames', {'k16'});
set(p19, 'Value', 1000.0);
set(p19, 'ValueUnits', '1/second');

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(r7, 'Reaction', 'Heat_shock.HSP90 + Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r1, 'Reaction', 'Heat_shock.NatP -> Heat_shock.MisP');
set(r4, 'Reaction', 'Heat_shock.[HSP90&MisP] -> Heat_shock.HSP90 + Heat_shock.NatP');
set(r2, 'Reaction', 'Heat_shock.MisP -> Heat_shock.AggP');
set(r8, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.DiH');
set(r5, 'Reaction', 'Heat_shock.MisP -> null');
set(r3, 'Reaction', 'Heat_shock.MisP + Heat_shock.HSP90 <-> Heat_shock.[HSP90&MisP]');
set(r6, 'Reaction', 'null -> Heat_shock.NatP');
set(r9, 'Reaction', 'Autoregulation.DiH + Autoregulation.HSF1 <-> Autoregulation.TriH');
set(r10, 'Reaction', 'Autoregulation.TriH + Autoregulation.HSE <-> Autoregulation.[TriH&HSE]');
set(r11, 'Reaction', 'Autoregulation.[TriH&HSE] -> Autoregulation.[TriH&HSE] + Heat_shock.HSP90');

% Delete object(s).
delete(m1.Compartments(3).Species(1));
delete(m1.Compartments(3));

% Configure properties.
set(r8, 'ReactionRate', 'k10*(Autoregulation.HSF1)^2 - k13*Autoregulation.DiH');

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);
set(r8, 'ReactionRate', 'k10*(Autoregulation.HSF1) - k13*Autoregulation.DiH');
set(r8, 'ReactionRate', 'k10*Autoregulation.HSF1 - k13*Autoregulation.DiH');
set(k8, 'KineticLawName', 'MassAction');
set(k8, 'ParameterVariableNames', {'k10','k13'});
set(r8, 'Reversible', true);
set(r8, 'Reaction', 'Autoregulation.HSF1 + Autoregulation.HSF1 <-> Autoregulation.DiH');
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(c2, 'CapacityUnits', 'microlitre');

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(s9, 'InitialAmountUnits', 'molarity');

% Verify the SimBiology Model.
verify(m1);
verify(m1);

% Configure properties.
set(s10, 'InitialAmountUnits', 'molarity');

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(s12, 'InitialAmountUnits', 'molarity');
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 100.0);
set(cs1, 'StopTime', 10.0);
set(cs1, 'StopTime', 10.0);

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(s6, 'InitialAmountUnits', 'molarity');
set(s8, 'InitialAmountUnits', 'molarity');
set(cs1.CompileOptions, 'UnitConversion', false);
set(cs1.CompileOptions, 'UnitConversion', false);

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(s11, 'InitialAmountUnits', 'molarity');

% Verify the SimBiology Model.
verify(m1);

% Configure properties.
set(r7, 'Reaction', 'Heat_shock.HSP90 + Autoregulation.HSF1 <-> null');
set(r7, 'Reversible', true);
set(r7, 'Reaction', 'Heat_shock.HSP90 + Autoregulation.HSF1 <-> null');
set(r7, 'Reaction', 'Heat_shock.HSP90 <-> null');
set(r7, 'Reversible', true);
set(r7, 'Reaction', 'Heat_shock.HSP90 <-> null');
set(r8, 'Reaction', 'null <-> Autoregulation.DiH');
set(r8, 'Reversible', true);
set(r8, 'Reaction', 'null <-> Autoregulation.DiH');
set(r9, 'Reaction', 'Autoregulation.DiH <-> Autoregulation.TriH');
set(r9, 'Reversible', true);
set(r9, 'Reaction', 'Autoregulation.DiH <-> Autoregulation.TriH');
set(r10, 'Reaction', 'Autoregulation.TriH <-> Autoregulation.[TriH&HSE]');
set(r10, 'Reversible', true);
set(r10, 'Reaction', 'Autoregulation.TriH <-> Autoregulation.[TriH&HSE]');
set(r8, 'Reaction', 'null <-> null');
set(r8, 'Reversible', true);
set(r8, 'Reaction', 'null <-> null');
set(r9, 'Reaction', 'null <-> Autoregulation.TriH');
set(r9, 'Reversible', true);
set(r9, 'Reaction', 'null <-> Autoregulation.TriH');
set(r9, 'Reaction', 'null <-> null');
set(r9, 'Reversible', true);
set(r9, 'Reaction', 'null <-> null');
set(r10, 'Reaction', 'null <-> Autoregulation.[TriH&HSE]');
set(r10, 'Reversible', true);
set(r10, 'Reaction', 'null <-> Autoregulation.[TriH&HSE]');
set(r10, 'Reaction', 'null <-> null');
set(r10, 'Reversible', true);
set(r10, 'Reaction', 'null <-> null');
set(r11, 'Reaction', 'null -> Autoregulation.[TriH&HSE] + Heat_shock.HSP90');
set(r11, 'Reaction', 'null -> Heat_shock.HSP90');
set(r11, 'Reversible', false);
set(r11, 'Reaction', 'null -> Heat_shock.HSP90');
set(r7, 'Reaction', 'HSP90 <-> null');
set(r1, 'Reaction', 'NatP -> MisP');
set(r4, 'Reaction', '[HSP90&MisP] -> HSP90 + NatP');
set(r2, 'Reaction', 'MisP -> AggP');
set(r8, 'Reaction', 'null <-> null');
set(r5, 'Reaction', 'MisP -> null');
set(r3, 'Reaction', 'MisP + HSP90 <-> [HSP90&MisP]');
set(r6, 'Reaction', 'null -> NatP');
set(r9, 'Reaction', 'null <-> null');
set(r10, 'Reaction', 'null <-> null');
set(r11, 'Reaction', 'null -> HSP90');

% Delete object(s).
delete(m1.Compartments(2).Species(2));
delete(m1.Compartments(2).Species(1));
delete(m1.Compartments(2).Species(3));
delete(m1.Compartments(2).Species(1));
delete(m1.Compartments(2).Species(1));
delete(m1.Compartments(2).Species(1));
delete(m1.Compartments(2));
delete(m1.Reactions(9));
delete(m1.Reactions(10));
delete(m1.Reactions(7));
delete(m1.Reactions(8));
delete(m1.Reactions(11));

% Import SimBiology Model from MATLAB workspace. Note 
% that the following call may return an array of models. 
% Index into the array to retrieve the desired model.
m2 = sbioselect('Type', 'sbiomodel', 'Name', 'heat_shock_re');

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm2');

% Import SimBiology Model from MATLAB workspace. Note 
% that the following call may return an array of models. 
% Index into the array to retrieve the desired model.
m3 = sbioselect('Type', 'sbiomodel', 'Name', 'heat_shock_re');

% Assign variable name to object.
r13 = m3.Reactions(7);

% Configure properties.
set(r13, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r13, 'Reversible', true);
set(r13, 'Reaction', 'Autoregulation.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r13, 'Reaction', 'null <-> Autoregulation.[HSF1&HSP90]');
set(r13, 'Reversible', true);
set(r13, 'Reaction', 'null <-> Autoregulation.[HSF1&HSP90]');
set(r13, 'Reaction', 'null <-> Autoregulation.[HSF1&HSP90]');
set(r13, 'Reversible', true);
set(r13, 'Reaction', 'null <-> Autoregulation.[HSF1&HSP90]');
set(r13, 'Reaction', 'null <-> null');
set(r13, 'Reversible', true);
set(r13, 'Reaction', 'null <-> null');

% Delete object(s).
delete(m3.Compartments(2).Species(1));
delete(m3.Compartments(2).Species(1));
delete(m3.Compartments(2).Species(1));
delete(m3.Reactions(7));

% Assign variable name to object.
c4 = m3.Compartments(2);

% Add component(s) to SimBiology Model.
s17 = addspecies(c4, 'HSF1&HSP90');
s18 = addspecies(c4, 'HSP90');
s19 = addspecies(c4, 'HSF1');
r14 = addreaction(m3, 'Autoregulation.HSF1 + Autoregulation.HSP90 <-> Autoregulation.[HSF1&HSP90]');

% Configure properties.
set(r14, 'Name', 'reaction_1');
set(r14, 'KineticLaw', 'KineticLaw');

% Add kinetic law object to the reaction.
k13 = addkineticlaw(r14, 'MassAction');

% Add component(s) to SimBiology Model.
p21 = addparameter(k13, 'k8', 1.0);

% Configure properties.
set(p21, 'ValueUnits', '1/(molarity*second)');

% Add component(s) to SimBiology Model.
p22 = addparameter(k13, 'k9', 1.0);

% Configure properties.
set(p22, 'ValueUnits', '1/second');
set(k13, 'ParameterVariableNames', {'k8','k9'});
set(r14, 'Reaction', 'Autoregulation.HSP90 <-> Autoregulation.[HSF1&HSP90]');
set(r14, 'Reversible', true);
set(r14, 'Reaction', 'Autoregulation.HSP90 <-> Autoregulation.[HSF1&HSP90]');

% Assign variable name to object.
c5 = m3.Compartments(1);

% Add component(s) to SimBiology Model.
s20 = addspecies(c5, 'HSF1');

% Configure properties.
set(r14, 'Reaction', 'Autoregulation.HSP90 + Heat_shock.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r14, 'Reversible', true);
set(r14, 'Reaction', 'Autoregulation.HSP90 + Heat_shock.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r14, 'Reaction', 'Heat_shock.HSF1 <-> Autoregulation.[HSF1&HSP90]');
set(r14, 'Reversible', true);
set(r14, 'Reaction', 'Heat_shock.HSF1 <-> Autoregulation.[HSF1&HSP90]');

% Add component(s) to SimBiology Model.
s21 = addspecies(c5, 'HSP90_1');

% Configure properties.
set(r14, 'Reaction', 'Heat_shock.HSF1 + Heat_shock.HSP90_1 <-> Autoregulation.[HSF1&HSP90]');
set(r14, 'Reversible', true);
set(r14, 'Reaction', 'Heat_shock.HSF1 + Heat_shock.HSP90_1 <-> Autoregulation.[HSF1&HSP90]');
set(r14, 'Reaction', 'Heat_shock.HSF1 + Heat_shock.HSP90_1 <-> null');
set(r14, 'Reversible', true);
set(r14, 'Reaction', 'Heat_shock.HSF1 + Heat_shock.HSP90_1 <-> null');

% Add component(s) to SimBiology Model.
s22 = addspecies(c5, 'HSF1&HSP90');

% Configure properties.
set(r14, 'Reaction', 'Heat_shock.HSF1 + Heat_shock.HSP90_1 <-> Heat_shock.[HSF1&HSP90]');
set(r14, 'Reversible', true);
set(r14, 'Reaction', 'Heat_shock.HSF1 + Heat_shock.HSP90_1 <-> Heat_shock.[HSF1&HSP90]');

% Assign variable name to object.
r15 = m3.Reactions(1);

% Configure properties.
set(r15, 'Reaction', 'NatP -> MisP');

% Assign variable name to object.
r16 = m3.Reactions(3);

% Configure properties.
set(r16, 'Reaction', 'MisP + HSP90 <-> [HSP90&MisP]');

% Assign variable name to object.
r17 = m3.Reactions(2);

% Configure properties.
set(r17, 'Reaction', 'MisP -> AggP');

% Assign variable name to object.
r18 = m3.Reactions(4);

% Configure properties.
set(r18, 'Reaction', '[HSP90&MisP] -> HSP90 + NatP');

% Assign variable name to object.
r19 = m3.Reactions(5);

% Configure properties.
set(r19, 'Reaction', 'MisP -> null');

% Assign variable name to object.
r20 = m3.Reactions(6);

% Configure properties.
set(r20, 'Reaction', 'null -> NatP');
set(r14, 'Reaction', 'HSF1 + HSP90_1 <-> [HSF1&HSP90]');

% Delete object(s).
delete(m3.Compartments(2));

% Configure properties.
set(r14, 'Reversible', true);
set(r14, 'Reaction', 'HSF1 + HSP90 <-> [HSF1&HSP90]');

% Delete object(s).
delete(m3.Compartments(1).Species(7));

% Add component(s) to SimBiology Model.
s23 = addspecies(c5, 'species_1');
s24 = addspecies(c5, 'species_2');
s25 = addspecies(c5, 'species_3');
s26 = addspecies(c5, 'species_4');

% Rename component.
rename(s23, 'DiH');
rename(s24, 'TriH');

% Add component(s) to SimBiology Model.
r21 = addreaction(m3, 'HSF1 -> DiH');

% Configure properties.
set(r21, 'Name', 'reaction_2');
set(r21, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k14 = m3.Reactions(8).KineticLaw(1);

% Add component(s) to SimBiology Model.
p23 = addparameter(k14, 'kf', 1.0);
r22 = addreaction(m3, 'DiH -> TriH');

% Configure properties.
set(r22, 'Name', 'reaction_3');
set(r22, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k15 = m3.Reactions(9).KineticLaw(1);

% Add component(s) to SimBiology Model.
p24 = addparameter(k15, 'kf', 1.0);
r23 = addreaction(m3, 'HSF1 -> TriH');

% Configure properties.
set(r23, 'Name', 'reaction_4');
set(r23, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k16 = m3.Reactions(10).KineticLaw(1);

% Add component(s) to SimBiology Model.
p25 = addparameter(k16, 'kf', 1.0);

% Delete object(s).
delete(m3.Reactions(10));

% Configure properties.
set(r22, 'Reaction', 'DiH + HSF1 -> TriH');
set(r22, 'Reversible', false);
set(r22, 'Reaction', 'DiH + HSF1 -> TriH');

% Rename component.
rename(r22, 'Trimerization');

% Add component(s) to SimBiology Model.
r24 = addreaction(m3, 'TriH -> species_3');

% Configure properties.
set(r24, 'Name', 'reaction_3');
set(r24, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k17 = m3.Reactions(10).KineticLaw(1);

% Add component(s) to SimBiology Model.
p26 = addparameter(k17, 'kf', 1.0);

% Delete object(s).
delete(m3.Reactions(10));

% Add component(s) to SimBiology Model.
r25 = addreaction(m3, 'TriH -> species_4');

% Configure properties.
set(r25, 'Name', 'reaction_3');
set(r25, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k18 = m3.Reactions(10).KineticLaw(1);

% Add component(s) to SimBiology Model.
p27 = addparameter(k18, 'kf', 1.0);

% Configure properties.
set(r25, 'Reaction', 'TriH + species_3 -> species_4');
set(r25, 'Reversible', false);
set(r25, 'Reaction', 'TriH + species_3 -> species_4');

% Rename component.
rename(s25, 'HSE');
rename(s26, 'TriH&HSE');
rename(r14, 'HSF1 binding');
rename(r21, 'Dimerization');
rename(r25, 'DNA binding');

% Add component(s) to SimBiology Model.
r26 = addreaction(m3, '[TriH&HSE] -> HSP90');

% Configure properties.
set(r26, 'Name', 'reaction_1');
set(r26, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k19 = m3.Reactions(11).KineticLaw(1);

% Add component(s) to SimBiology Model.
p28 = addparameter(k19, 'kf', 1.0);

% Rename component.
rename(r26, 'Synthesis');

% Configure properties.
set(r26, 'Reversible', false);
set(r26, 'Reaction', '[TriH&HSE] -> HSP90 + [TriH&HSE]');
set(r21, 'Reaction', 'HSF1 <-> DiH');
set(r21, 'Reversible', true);
set(p23, 'Name', 'k10');
set(k14, 'ParameterVariableNames', {'k10',''});

% Add component(s) to SimBiology Model.
p29 = addparameter(k14, 'k13', 1.0);

% Configure properties.
set(k14, 'ParameterVariableNames', {'k10','k13'});
set(r21, 'ReactionRate', 'k10*HSF1*HSF1 - k13*DiH');
set(r22, 'Reaction', 'DiH + HSF1 <-> TriH');
set(r22, 'Reversible', true);
set(p24, 'Name', 'k11');
set(k15, 'ParameterVariableNames', {'k11',''});

% Add component(s) to SimBiology Model.
p30 = addparameter(k15, 'k12', 1.0);

% Configure properties.
set(k15, 'ParameterVariableNames', {'k11','k12'});
set(r25, 'Reaction', 'TriH + HSE <-> [TriH&HSE]');
set(r25, 'Reversible', true);
set(p27, 'Name', 'k14');
set(k18, 'ParameterVariableNames', {'k14',''});

% Add component(s) to SimBiology Model.
p31 = addparameter(k18, 'k15', 1.0);

% Configure properties.
set(k18, 'ParameterVariableNames', {'k14','k15'});

% Add component(s) to SimBiology Model.
r27 = addreaction(m3, 'null -> null');

% Configure properties.
set(r27, 'Name', 'reaction_1');
set(r27, 'Reaction', 'HSP90 -> null');
set(r27, 'Reversible', false);
set(r27, 'Reaction', 'HSP90 -> null');
set(r27, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k20 = m3.Reactions(12).KineticLaw(1);

% Add component(s) to SimBiology Model.
p32 = addparameter(k20, 'kf', 1.0);

% Configure properties.
set(p32, 'Name', 'k17');
set(k20, 'ParameterVariableNames', {'k17'});

% Add component(s) to SimBiology Model.
s27 = addspecies(c5, 'species_1');

% Rename component.
rename(s27, 'ATP');

% Add component(s) to SimBiology Model.
s28 = addspecies(c5, 'ATP1');

% Rename component.
rename(s28, 'ADP');

% Add component(s) to SimBiology Model.
s29 = addspecies(c5, 'species_1');

% Rename component.
rename(s29, 'ROS');
rename(r27, 'degradation');

% Add component(s) to SimBiology Model.
r28 = addreaction(m3, 'ATP -> MisP');

% Configure properties.
set(r28, 'Name', 'reaction_1');
set(r28, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k21 = m3.Reactions(13).KineticLaw(1);

% Add component(s) to SimBiology Model.
p33 = addparameter(k21, 'kf', 1.0);

% Delete object(s).
delete(m3.Reactions(13));

% Configure properties.
set(r19, 'Reaction', 'MisP + ATP -> null');
set(r19, 'Reversible', false);
set(r19, 'Reaction', 'MisP + ATP -> null');
set(r19, 'Reaction', 'MisP + ATP -> ADP');
set(r19, 'Reversible', false);
set(r19, 'Reaction', 'MisP + ATP -> ADP');
set(r27, 'Reaction', 'HSP90 + ATP -> null');
set(r27, 'Reversible', false);
set(r27, 'Reaction', 'HSP90 + ATP -> null');
set(r27, 'Reaction', 'HSP90 + ATP -> ADP');
set(r27, 'Reversible', false);
set(r27, 'Reaction', 'HSP90 + ATP -> ADP');
set(r18, 'Reaction', '[HSP90&MisP] + ATP -> HSP90 + NatP');
set(r18, 'Reversible', false);
set(r18, 'Reaction', '[HSP90&MisP] + ATP -> HSP90 + NatP');
set(r18, 'Reaction', '[HSP90&MisP] + ATP -> HSP90 + NatP + ADP');
set(r18, 'Reversible', false);
set(r18, 'Reaction', '[HSP90&MisP] + ATP -> HSP90 + NatP + ADP');
set(r15, 'Reaction', 'NatP + ROS -> MisP');
set(r15, 'Reversible', false);
set(r15, 'Reaction', 'NatP + ROS -> MisP');
set(r15, 'Reversible', false);
set(r15, 'Reaction', 'NatP + ROS -> MisP + ROS');
set(s25, 'InitialAmount', 1.6605391E-21);
set(s25, 'InitialAmountUnits', 'molarity');
set(s22, 'InitialAmount', 9.7971805E-18);
set(s22, 'InitialAmountUnits', 'molarity');
set(s20, 'InitialAmount', 100.0);
set(s20, 'InitialAmountUnits', '1.6605391e-19');
set(s20, 'InitialAmount', 1.6605391E-19);
set(s20, 'InitialAmountUnits', 'molarity');
set(s29, 'InitialAmount', 1.6605391E-19);
set(s29, 'InitialAmountUnits', 'molarity');
set(s27, 'InitialAmount', 1.6605391E-17);
set(s27, 'InitialAmountUnits', 'Molarity');
set(s27, 'InitialAmountUnits', 'molarity');
set(s28, 'InitialAmount', 1.6605391E-18);
set(s28, 'InitialAmountUnits', 'molarity');

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');

% Configure properties.
set(p32, 'Value', 8.02E-9);
set(p32, 'Value', 1.0);
set(p32, 'ValueUnits', '1/second');
set(p32, 'Value', 8.02E-9);
set(p32, 'Value', 1.0);
set(p32, 'Value', 8.02E-9);
set(p23, 'Value', 0.01);
set(p23, 'ValueUnits', '1/(molarity*second)');
set(p29, 'Value', 0.5);
set(p29, 'ValueUnits', '1/second');
set(p27, 'Value', 0.05);
set(p27, 'ValueUnits', '1/(molarity*second)');
set(p31, 'Value', 0.08);
set(p31, 'ValueUnits', '1/second');
set(p21, 'Value', 500.0);
set(p28, 'Name', 'k16');
set(k19, 'ParameterVariableNames', {'k16'});
set(p28, 'Value', 1000.0);
set(p28, 'ValueUnits', '1/second');
set(p24, 'Value', 100.0);
set(p30, 'Value', 0.5);
set(p24, 'ValueUnits', '1/(molarity*second)');
set(p30, 'ValueUnits', '1/second');

% Add component(s) to SimBiology Model.
r29 = addreaction(m3, 'ADP -> ATP');

% Assign variable name to object.
k22 = m3.Reactions(13).KineticLaw(1);

% Add component(s) to SimBiology Model.
p34 = addparameter(k22, 'kf', 1.0);

% Rename component.
rename(r29, 'generation');

% Configure properties.
set(p34, 'Name', 'k18');
set(k22, 'ParameterVariableNames', {'k18'});
set(p34, 'Value', 12.0);
set(p34, 'ValueUnits', '1/second');

% Add component(s) to SimBiology Model.
r30 = addreaction(m3, 'null -> null');

% Configure properties.
set(r30, 'Reaction', 'null -> ROS');
set(r30, 'Reversible', false);
set(r30, 'Reaction', 'null -> ROS');
set(r30, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k23 = m3.Reactions(14).KineticLaw(1);

% Add component(s) to SimBiology Model.
p35 = addparameter(k23, 'kf', 1.0);

% Rename component.
rename(r30, 'ROS production');

% Configure properties.
set(p35, 'Name', 'k20');
set(k23, 'ParameterVariableNames', {'k20'});
set(p35, 'Value', 0.1);
set(p35, 'ValueUnits', 'molarity/second');

% Add component(s) to SimBiology Model.
r31 = addreaction(m3, 'null -> null');

% Rename component.
rename(r31, 'ROS Removal');

% Configure properties.
set(r31, 'Reaction', 'ROS -> null');
set(r31, 'Reversible', false);
set(r31, 'Reaction', 'ROS -> null');
set(r31, 'KineticLaw', 'KineticLaw');

% Assign variable name to object.
k24 = m3.Reactions(15).KineticLaw(1);

% Add component(s) to SimBiology Model.
p36 = addparameter(k24, 'kf', 1.0);

% Configure properties.
set(p36, 'Name', 'k21');
set(k24, 'ParameterVariableNames', {'k21'});
set(p36, 'Value', 0.001);
set(p36, 'ValueUnits', '1/second');

% Verify the SimBiology Model.
verify(m3);

% Configure properties.
set(s23, 'InitialAmountUnits', 'molarity');
set(r15, 'ReactionRate', 'k2*NatP');

% Assign variable name to object.
p37 = m3.Reactions(1).KineticLaw(1).Parameters(1);

% Configure properties.
set(p37, 'ConstantValue', false);
set(p37, 'ConstantValue', true);

% Verify the SimBiology Model.
verify(m3);

% Configure properties.
set(s24, 'InitialAmountUnits', 'molarity');

% Verify the SimBiology Model.
verify(m3);

% Configure properties.
set(s26, 'InitialAmountUnits', 'molarity');

% Verify the SimBiology Model.
verify(m3);

% Configure properties.
set(r18, 'ReactionRate', 'k5*[HSP90&MisP]');
set(r19, 'ReactionRate', 'k6*MisP');
set(r27, 'ReactionRate', 'k17*HSP90');

% Verify the SimBiology Model.
verify(m3);

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');

% Assign variable name to object.
cs2 = getconfigset(m3, 'default');

% Configure properties.
set(cs2, 'StopTime', 100.0);
set(cs2, 'StopTime', 10.0);

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');

% Configure properties.
set(cs2, 'StopTime', 1000.0);
set(cs2, 'StopTime', 10.0);

% Save SimBiology project.
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');
sbiosaveproject('C:\Users\LZL\OneDrive - UNSW\iGEM\Modeling-Tutorials\heat_shock_re.sbproj', 'm3');

% Assign variable name to object.
k25 = m3.Reactions(1).KineticLaw(1);

% Configure properties.
set(k25, 'KineticLawName', 'MassAction');

% Assign variable name to object.
k25 = m3.Reactions(1).KineticLaw(1);

% Configure properties.
set(k25, 'ParameterVariableNames', {'k2'});
set(k25, 'KineticLawName', 'Unknown');
set(r15, 'ReactionRate', 'k2*NatP');
set(s28, 'InitialAmountUnits', 'molecules');
set(s28, 'InitialAmountUnits', 'molecule');
set(s28, 'InitialAmount', 600000.0);
set(cs2, 'StopTime', 1000.0);
set(cs2, 'StopTime', 10.0);
set(cs2, 'SolverType', 'ssa');
set(cs2, 'StopTime', 1000.0);
set(cs2, 'StopTime', 10.0);
set(cs2, 'SolverType', 'ode15s');
set(cs2, 'StopTime', 1000.0);
set(cs2, 'StopTime', 10.0);

% Assign variable name to object.
p38 = m3.Reactions(2).KineticLaw(1).Parameters(1);

% Configure properties.
set(p38, 'ConstantValue', false);
set(p38, 'ConstantValue', true);